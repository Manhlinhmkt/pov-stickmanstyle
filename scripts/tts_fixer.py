#!/usr/bin/env python
"""
TTS Fixer for Biblical Wisdom Episodes
Fixes scripture colon-notation (e.g., "Romans 12:6" → "Romans chapter twelve, verse six")
in vo_script_table.csv files.
"""

import csv
import re
import sys
from pathlib import Path

# Number word mapping
ONES = {
    '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
    '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine',
    '10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen',
    '14': 'fourteen', '15': 'fifteen', '16': 'sixteen', '17': 'seventeen',
    '18': 'eighteen', '19': 'nineteen'
}
TENS = {
    '2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty',
    '6': 'sixty', '7': 'seventy', '8': 'eighty', '9': 'ninety'
}


def number_to_words(n_str: str) -> str:
    """Convert a number string to words (supports 1-199)."""
    n = int(n_str)
    if n < 20:
        return ONES[str(n)]
    elif n < 100:
        tens = TENS[str(n // 10)]
        ones = n % 10
        if ones == 0:
            return tens
        return f"{tens}-{ONES[str(ones)]}"
    elif n < 200:
        remainder = n - 100
        if remainder == 0:
            return "one hundred"
        return f"one hundred {number_to_words(str(remainder))}"
    return n_str  # fallback


def fix_scripture_colon(text: str) -> str:
    """Fix scripture shorthand:
    1. Colon-notation like 'Romans 12:6' → 'Romans chapter twelve, verse six'
    2. Numeric digits after chapter/verse like 'chapter 2' → 'chapter two'
    """
    # === PASS 1: Colon-notation (Book N:N) ===
    def replace_colon(m):
        prefix = m.group(1)  # e.g., "Second Timothy " or "Romans "
        chapter = m.group(2)  # e.g., "12"
        verse_part = m.group(3)  # e.g., "6" or "29-30"
        
        chapter_word = number_to_words(chapter)
        
        # Handle verse ranges (e.g., "29-30")
        if '-' in verse_part:
            parts = verse_part.split('-')
            v_start = number_to_words(parts[0])
            v_end = number_to_words(parts[1])
            return f"{prefix}chapter {chapter_word}, verses {v_start} through {v_end}"
        else:
            verse_word = number_to_words(verse_part)
            return f"{prefix}chapter {chapter_word}, verse {verse_word}"
    
    colon_pattern = re.compile(
        r'((?:(?:First|Second|Third|1st|2nd|3rd|1|2|3)\s+)?'
        r'(?:Genesis|Exodus|Leviticus|Numbers|Deuteronomy|Joshua|Judges|Ruth|'
        r'Samuel|Kings|Chronicles|Ezra|Nehemiah|Esther|Job|Psalms?|Proverbs|'
        r'Ecclesiastes|Song\s+of\s+Solomon|Isaiah|Jeremiah|Lamentations|'
        r'Ezekiel|Daniel|Hosea|Joel|Amos|Obadiah|Jonah|Micah|Nahum|'
        r'Habakkuk|Zephaniah|Haggai|Zechariah|Malachi|'
        r'Matthew|Mark|Luke|John|Acts|Romans|Corinthians|Galatians|'
        r'Ephesians|Philippians|Colossians|Thessalonians|Timothy|Titus|'
        r'Philemon|Hebrews|James|Peter|Jude|Revelation)'
        r'\s+)'
        r'(\d+):(\d+(?:-\d+)?)',
        re.IGNORECASE
    )
    
    text = colon_pattern.sub(replace_colon, text)
    
    # === PASS 2: Numeric digits after chapter/verse/verses keywords ===
    def replace_keyword_digit(m):
        keyword = m.group(1)  # "chapter", "verse", or "verses"
        number = m.group(2)   # e.g., "2", "43"
        return f"{keyword} {number_to_words(number)}"
    
    keyword_digit_pattern = re.compile(
        r'\b(chapter|verses?)\s+(\d+)',
        re.IGNORECASE
    )
    
    text = keyword_digit_pattern.sub(replace_keyword_digit, text)
    
    # === PASS 3: Trailing digits after and/through/to in verse contexts ===
    # e.g., "verses twenty-two and 23" → "verses twenty-two and twenty-three"
    # e.g., "through 30" → "through thirty"
    def replace_trailing_digit(m):
        conjunction = m.group(1)  # "and", "through", "to"
        number = m.group(2)
        return f"{conjunction} {number_to_words(number)}"
    
    trailing_digit_pattern = re.compile(
        r'\b(and|through|to)\s+(\d+)\b'
    )
    
    text = trailing_digit_pattern.sub(replace_trailing_digit, text)
    
    return text


def fix_episode(episode_dir: Path, dry_run: bool = False) -> dict:
    """Fix scripture colon-notation in an episode's vo_script_table.csv."""
    vo_path = episode_dir / "vo_script_table.csv"
    if not vo_path.exists():
        return {'status': 'SKIP', 'reason': 'No vo_script_table.csv'}
    
    # Read
    with open(vo_path, 'r', encoding='utf-8-sig') as f:
        content = f.read()
    
    reader = csv.DictReader(content.splitlines())
    fieldnames = reader.fieldnames
    rows = list(reader)
    
    fixes = []
    for i, row in enumerate(rows):
        vo_en = row.get('VO_EN', '')
        fixed = fix_scripture_colon(vo_en)
        if fixed != vo_en:
            fixes.append({
                'line': i + 2,
                'vo_id': row.get('VO_ID', ''),
                'before': vo_en,
                'after': fixed
            })
            row['VO_EN'] = fixed
    
    if not fixes:
        return {'status': 'CLEAN', 'fixes': 0}
    
    if not dry_run:
        with open(vo_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            writer.writeheader()
            writer.writerows(rows)
    
    return {'status': 'FIXED', 'fixes': len(fixes), 'details': fixes}


def main():
    """Main entry point."""
    dry_run = '--dry-run' in sys.argv
    args = [a for a in sys.argv[1:] if a != '--dry-run']
    
    if not args:
        print("Usage: python tts_fixer.py <episode_dir> [--dry-run]")
        print("       python tts_fixer.py --all [--dry-run]")
        sys.exit(1)
    
    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent
    
    if args[0] == '--all':
        episodes_dir = project_root / "episodes"
        episode_dirs = sorted([
            d for d in episodes_dir.iterdir()
            if d.is_dir() and (d / "vo_script_table.csv").exists()
        ])
    else:
        ep = Path(args[0])
        if not ep.is_absolute():
            ep = project_root / ep
        episode_dirs = [ep]
    
    mode = "DRY RUN" if dry_run else "FIX"
    print(f"\n{'=' * 60}")
    print(f"TTS FIXER [{mode}]")
    print(f"{'=' * 60}\n")
    
    total_fixes = 0
    for ep_dir in episode_dirs:
        result = fix_episode(ep_dir, dry_run=dry_run)
        ep_name = ep_dir.name
        
        if result['status'] == 'CLEAN':
            print(f"  ✅ {ep_name}: No fixes needed")
        elif result['status'] == 'FIXED':
            total_fixes += result['fixes']
            print(f"  🔧 {ep_name}: {result['fixes']} fix(es)")
            for d in result['details']:
                print(f"       Line {d['line']} (VO_{d['vo_id']}): {d['before'][:60]}...")
                print(f"       → {d['after'][:60]}...")
        elif result['status'] == 'SKIP':
            print(f"  ⏭️  {ep_name}: {result['reason']}")
    
    print(f"\n{'=' * 60}")
    print(f"Total fixes: {total_fixes}")
    print(f"{'=' * 60}\n")


if __name__ == "__main__":
    main()
