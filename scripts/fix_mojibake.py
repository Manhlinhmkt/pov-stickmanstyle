#!/usr/bin/env python3
"""
Fix Encoding Script - Repair mojibake + sanitize Unicode dashes in episode files.

Modes:
  SCAN      - detect mojibake (default)
  --fix     - repair mojibake (cp1252 reverse + pattern replacement)
  --sanitize - replace Unicode dashes/quotes with ASCII equivalents (preventive)

Usage:
    python scripts/fix_mojibake.py                      # scan all episodes
    python scripts/fix_mojibake.py PV_0009               # scan specific episode
    python scripts/fix_mojibake.py --fix                 # fix mojibake in all
    python scripts/fix_mojibake.py --fix PV_0009         # fix specific episode
    python scripts/fix_mojibake.py --sanitize            # sanitize all episodes
    python scripts/fix_mojibake.py --sanitize PV_0009    # sanitize specific episode
"""
import os
import sys
import glob
import shutil
from datetime import datetime

EPISODES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "pvle", "episodes")

# ============================================================
# MOJIBAKE REPLACEMENT MAP
# Key = mojibake sequence, Value = correct character
# These occur when UTF-8 bytes are decoded as cp1252 then re-encoded as UTF-8
# ============================================================
MOJIBAKE_MAP = {
    # Punctuation
    "\u00e2\u20ac\u201d": " - ",    # em dash U+2014 -> replace with spaced hyphen
    "\u00e2\u20ac\u201c": " - ",    # en dash U+2013 -> replace with spaced hyphen
    "\u00e2\u20ac\u2122": "'",       # right single quote U+2019
    "\u00e2\u20ac\u0153": '"',       # left double quote U+201C
    "\u00e2\u20ac\u009d": '"',       # right double quote U+201D
    "\u00e2\u20ac\u2026": "...",     # ellipsis U+2026
    "\u00e2\u20ac\u0094": " - ",    # another em dash variant
    
    # Vietnamese diacritics (double-encoded)
    "\u00c3\u00a1": "\u00e1",   # a-acute
    "\u00c3\u00a0": "\u00e0",   # a-grave
    "\u00c3\u00a2": "\u00e2",   # a-circumflex
    "\u00c3\u00a3": "\u00e3",   # a-tilde
    "\u00c3\u00a4": "\u00e4",   # a-diaeresis
    "\u00c3\u00a9": "\u00e9",   # e-acute
    "\u00c3\u00a8": "\u00e8",   # e-grave
    "\u00c3\u00aa": "\u00ea",   # e-circumflex
    "\u00c3\u00ad": "\u00ed",   # i-acute
    "\u00c3\u00ac": "\u00ec",   # i-grave
    "\u00c3\u00b3": "\u00f3",   # o-acute
    "\u00c3\u00b2": "\u00f2",   # o-grave
    "\u00c3\u00b4": "\u00f4",   # o-circumflex
    "\u00c3\u00b5": "\u00f5",   # o-tilde
    "\u00c3\u00ba": "\u00fa",   # u-acute
    "\u00c3\u00b9": "\u00f9",   # u-grave
    "\u00c3\u00bc": "\u00fc",   # u-umlaut
    "\u00c3\u00bd": "\u00fd",   # y-acute
    "\u00c4\u0192": "\u0103",   # a-breve (Vietnamese)
    "\u00c6\u00b0": "\u01b0",   # u-horn (Vietnamese)
    "\u00c6\u00a1": "\u01a1",   # o-horn (Vietnamese)
    "\u00c4\u0090": "\u0110",   # D-stroke (Vietnamese)
    "\u00c4\u2018": "\u0111",   # d-stroke (Vietnamese)
    
    # Japanese mojibake is harder to fix via simple replacement
    # Those files need cp1252->utf8 approach
}

# Detection patterns (subset for fast scanning)
DETECT_PATTERNS = [
    "\u00e2\u20ac\u201d",   # em dash mojibake
    "\u00e2\u20ac\u201c",   # en dash mojibake
    "\u00c3\u00a1",          # Vietnamese a-acute mojibake
    "\u00c3\u00a0",          # Vietnamese a-grave mojibake
    "\u00c3\u00aa",          # Vietnamese e-circumflex mojibake
]


def detect_mojibake(text):
    """Count total mojibake occurrences in text."""
    total = 0
    for pattern in DETECT_PATTERNS:
        total += text.count(pattern)
    return total


def fix_via_cp1252(text):
    """Try to fix by reversing double-encoding: encode as cp1252, decode as utf-8."""
    # Strip BOM first
    text = text.lstrip("\ufeff")
    try:
        fixed = text.encode("cp1252").decode("utf-8")
        return fixed, "cp1252_reverse"
    except (UnicodeEncodeError, UnicodeDecodeError):
        return None, None


def fix_via_replacement(text):
    """Fix by replacing known mojibake patterns."""
    text = text.lstrip("\ufeff")
    fixed = text
    replacements = 0
    for mojibake, correct in MOJIBAKE_MAP.items():
        count = fixed.count(mojibake)
        if count > 0:
            fixed = fixed.replace(mojibake, correct)
            replacements += count
    return fixed, replacements


def process_file(filepath, do_fix=False):
    """Scan or fix a single file. Returns (has_issues, was_fixed)."""
    fname = os.path.basename(filepath)
    ep_id = os.path.basename(os.path.dirname(filepath))
    
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    
    count = detect_mojibake(text)
    if count == 0:
        return False, False
    
    if not do_fix:
        print(f"  CORRUPT: {ep_id}/{fname} - {count} mojibake sequences found")
        return True, False
    
    # Try cp1252 reverse first (best quality)
    fixed, method = fix_via_cp1252(text)
    if fixed is not None:
        remaining = detect_mojibake(fixed)
        if remaining == 0:
            # Backup original
            backup = filepath + ".bak"
            shutil.copy2(filepath, backup)
            # Write fixed version with UTF-8 BOM
            with open(filepath, "w", encoding="utf-8-sig", newline="") as f:
                f.write(fixed)
            print(f"  FIXED ({method}): {ep_id}/{fname} - {count} mojibake resolved")
            return True, True
    
    # Fall back to pattern replacement
    fixed, replacements = fix_via_replacement(text)
    remaining = detect_mojibake(fixed)
    
    if replacements > 0:
        # Backup original
        backup = filepath + ".bak"
        shutil.copy2(filepath, backup)
        # Write fixed version with UTF-8 BOM
        with open(filepath, "w", encoding="utf-8-sig", newline="") as f:
            f.write(fixed)
        status = "FIXED" if remaining == 0 else "PARTIAL FIX"
        print(f"  {status} (replacement): {ep_id}/{fname} - {replacements} replaced, {remaining} remaining")
        return True, True
    
    print(f"  UNFIXABLE: {ep_id}/{fname} - {count} mojibake, no auto-fix available")
    return True, False


# ============================================================
# SANITIZE: Replace Unicode dashes/quotes with ASCII equivalents
# This is PREVENTIVE - works on clean (non-mojibake) files
# ============================================================
SANITIZE_MAP = {
    "\u2014": " - ",     # em dash -> spaced hyphen
    "\u2013": " - ",     # en dash -> spaced hyphen
    "\u2018": "'",        # left single quote -> ASCII apostrophe
    "\u2019": "'",        # right single quote -> ASCII apostrophe
    "\u201c": '"',        # left double quote -> ASCII double quote
    "\u201d": '"',        # right double quote -> ASCII double quote
    "\u2026": "...",      # horizontal ellipsis -> three dots
}


def sanitize_text(text):
    """Replace Unicode dashes/quotes with ASCII equivalents. Returns (sanitized_text, replacement_count)."""
    count = 0
    for unicode_char, ascii_char in SANITIZE_MAP.items():
        n = text.count(unicode_char)
        if n > 0:
            text = text.replace(unicode_char, ascii_char)
            count += n
    return text, count


def sanitize_file(filepath):
    """Sanitize a single file. Returns (had_issues, count)."""
    fname = os.path.basename(filepath)
    ep_id = os.path.basename(os.path.dirname(filepath))
    
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    
    sanitized, count = sanitize_text(text)
    
    if count == 0:
        return False, 0
    
    # Strip existing BOM and re-write with BOM
    sanitized = sanitized.lstrip("\ufeff")
    with open(filepath, "w", encoding="utf-8-sig", newline="") as f:
        f.write(sanitized)
    
    print(f"  SANITIZED: {ep_id}/{fname} - {count} Unicode chars replaced with ASCII")
    return True, count


def main():
    do_fix = "--fix" in sys.argv
    do_sanitize = "--sanitize" in sys.argv
    target_ep = None
    
    for arg in sys.argv[1:]:
        if arg.startswith("PV_"):
            target_ep = arg
    
    if do_sanitize:
        mode = "SANITIZE"
    elif do_fix:
        mode = "FIX"
    else:
        mode = "SCAN"
    
    print(f"\n{'=' * 60}")
    print(f"MOJIBAKE {mode} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'=' * 60}")
    
    if target_ep:
        ep_dirs = [os.path.join(EPISODES_DIR, target_ep)]
    else:
        ep_dirs = sorted(glob.glob(os.path.join(EPISODES_DIR, "PV_*")))
    
    total_issues = 0
    total_fixed = 0
    
    for ep_dir in ep_dirs:
        if not os.path.isdir(ep_dir):
            continue
        
        files = sorted(
            glob.glob(os.path.join(ep_dir, "*.csv")) + 
            glob.glob(os.path.join(ep_dir, "*.md"))
        )
        
        for filepath in files:
            if do_sanitize:
                had_issues, count = sanitize_file(filepath)
                if had_issues:
                    total_issues += 1
                    total_fixed += 1
            else:
                has_issues, was_fixed = process_file(filepath, do_fix)
                if has_issues:
                    total_issues += 1
                if was_fixed:
                    total_fixed += 1
    
    print(f"\n{'=' * 60}")
    if do_sanitize:
        print(f"RESULT: {total_fixed} files sanitized (Unicode -> ASCII punctuation)")
    elif do_fix:
        print(f"RESULT: {total_fixed}/{total_issues} files fixed")
        if total_fixed > 0:
            print("Backup files created with .bak extension")
    else:
        print(f"RESULT: {total_issues} files with encoding issues")
        if total_issues > 0:
            print("Run with --fix to repair: python scripts/fix_mojibake.py --fix")
    print(f"{'=' * 60}\n")


if __name__ == "__main__":
    main()

