#!/usr/bin/env python
"""
TTS Validator for Biblical Wisdom Episodes
Checks vo_script_table.csv against TTS formatting rules:
  - RULE_TTS_SCRIPTURE_SPELLING: No colon-notation scripture refs (e.g., 12:6)
  - RULE_TTS_MIN_WORDS: Every VO_EN line >= 2 words
  - RULE_ES_TRANSLATION: VO_ES column must exist
"""

import csv
import re
import sys
import yaml
from pathlib import Path
from typing import Dict, List, Any, Optional


# Regex patterns for scripture shorthand detection
# Matches patterns like "Romans 12:6", "1 John 4:18", "Hebrews 13:5"
SCRIPTURE_COLON_PATTERN = re.compile(
    r'\b(?:'
    r'(?:(?:First|Second|Third|1|2|3)\s+)?'  # Optional ordinal prefix
    r'(?:Genesis|Exodus|Leviticus|Numbers|Deuteronomy|Joshua|Judges|Ruth|'
    r'Samuel|Kings|Chronicles|Ezra|Nehemiah|Esther|Job|Psalms?|Proverbs|'
    r'Ecclesiastes|Song\s+of\s+Solomon|Isaiah|Jeremiah|Lamentations|'
    r'Ezekiel|Daniel|Hosea|Joel|Amos|Obadiah|Jonah|Micah|Nahum|'
    r'Habakkuk|Zephaniah|Haggai|Zechariah|Malachi|'
    r'Matthew|Mark|Luke|John|Acts|Romans|Corinthians|Galatians|'
    r'Ephesians|Philippians|Colossians|Thessalonians|Timothy|Titus|'
    r'Philemon|Hebrews|James|Peter|Jude|Revelation)'
    r'\s+)'                                    # Book name + space
    r'(\d+:\d+)',                               # Chapter:Verse (the violation)
    re.IGNORECASE
)

# Standalone colon pattern without book name (e.g., "chapter 12:6")
STANDALONE_COLON_PATTERN = re.compile(
    r'\b(?:chapter|ch\.?)\s+(\d+:\d+)',
    re.IGNORECASE
)

# Numeric digits after chapter/verse keywords (e.g., "chapter 2", "verse 1", "verses 15")
# These must be spelled out as words for TTS
CHAPTER_VERSE_DIGIT_PATTERN = re.compile(
    r'\b(chapter|verse|verses)\s+(\d+)',
    re.IGNORECASE
)


def load_csv(filepath: Path) -> List[Dict[str, str]]:
    """Load CSV file into list of dicts."""
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        return list(reader), reader.fieldnames


def count_words(text: str) -> int:
    """Count words in a string."""
    if not text or not text.strip():
        return 0
    return len(text.split())


def is_rhetorical_single_word(text: str) -> bool:
    """Check if a single-word line is an intentional rhetorical device.
    
    Exempts:
    - Single words ending with punctuation (e.g., "Nothing.", "Why?", "Amen.")
    - Stage directions like "[pause]"
    - These are deliberate dramatic devices, not TTS errors.
    """
    stripped = text.strip().strip('"').strip("'")
    if not stripped:
        return False
    # Stage directions in brackets
    if stripped.startswith('[') and stripped.endswith(']'):
        return True
    # Single word with ending punctuation (rhetorical device)
    if len(stripped.split()) == 1 and stripped[-1] in '.?!':
        return True
    return False


def check_scripture_shorthand(text: str) -> List[str]:
    """Find scripture shorthand violations in text."""
    violations = []
    # Check colon-notation (e.g., "Romans 12:6")
    for match in SCRIPTURE_COLON_PATTERN.finditer(text):
        violations.append(match.group(0))
    for match in STANDALONE_COLON_PATTERN.finditer(text):
        violations.append(match.group(0))
    # Check numeric digits after chapter/verse (e.g., "chapter 2", "verse 1")
    for match in CHAPTER_VERSE_DIGIT_PATTERN.finditer(text):
        violations.append(match.group(0))
    return violations


def validate_episode(episode_dir: Path) -> Dict[str, Any]:
    """
    Validate TTS rules for an episode.

    Args:
        episode_dir: Path to episode directory

    Returns:
        Validation report as dict
    """
    vo_path = episode_dir / "vo_script_table.csv"

    if not vo_path.exists():
        raise FileNotFoundError(f"VO script not found: {vo_path}")

    rows, fieldnames = load_csv(vo_path)
    episode_id = rows[0].get('Episode_ID', episode_dir.name) if rows else episode_dir.name

    # === CHECK 1: VO_ES Column Exists ===
    has_vo_es = 'VO_ES' in (fieldnames or [])

    # === CHECK 2 & 3: Per-line checks ===
    scripture_violations = []
    min_word_violations = []
    vo_es_empty_lines = []
    total_lines = len(rows)

    for i, row in enumerate(rows, start=2):  # line 2 = first data row (after header)
        vo_en = row.get('VO_EN', '')
        vo_id = row.get('VO_ID', str(i - 1))

        # Scripture shorthand check
        shorthand_hits = check_scripture_shorthand(vo_en)
        if shorthand_hits:
            scripture_violations.append({
                'line': i,
                'vo_id': vo_id,
                'matches': shorthand_hits,
                'text_snippet': vo_en[:80]
            })

        # Min words check (exempt rhetorical single-word lines)
        word_count = count_words(vo_en)
        if word_count < 2 and not is_rhetorical_single_word(vo_en):
            min_word_violations.append({
                'line': i,
                'vo_id': vo_id,
                'word_count': word_count,
                'text': vo_en
            })

        # VO_ES content check (only if column exists)
        if has_vo_es:
            vo_es = row.get('VO_ES', '')
            if not vo_es or not vo_es.strip():
                vo_es_empty_lines.append({
                    'line': i,
                    'vo_id': vo_id
                })

    # === Build Report ===
    rule_results = {
        'RULE_TTS_SCRIPTURE_SPELLING': {
            'status': 'PASS' if not scripture_violations else 'FAIL',
            'violation_count': len(scripture_violations),
            'details': scripture_violations
        },
        'RULE_TTS_MIN_WORDS': {
            'status': 'PASS' if not min_word_violations else 'FAIL',
            'violation_count': len(min_word_violations),
            'details': min_word_violations
        },
        'RULE_ES_TRANSLATION': {
            'status': 'PASS' if has_vo_es and not vo_es_empty_lines else 'INFO',
            'has_vo_es_column': has_vo_es,
            'empty_vo_es_count': len(vo_es_empty_lines) if has_vo_es else total_lines,
            'details': vo_es_empty_lines if has_vo_es else 'Column missing (optional)'
        }
    }

    # Only FAIL/PASS statuses count toward overall result (INFO is excluded)
    fail_count = sum(1 for r in rule_results.values() if r['status'] == 'FAIL')
    overall_status = 'PASS' if fail_count == 0 else 'FAIL'

    report = {
        'episode_id': episode_id,
        'file': str(vo_path),
        'total_vo_lines': total_lines,
        'schema_columns': fieldnames,
        'overall_status': overall_status,
        'rules_passed': 3 - fail_count,
        'rules_failed': fail_count,
        'rule_results': rule_results
    }

    return report


def save_report(report: Dict[str, Any], output_path: Path) -> None:
    """Save report as YAML."""
    with open(output_path, 'w', encoding='utf-8') as f:
        yaml.dump(report, f, default_flow_style=False, allow_unicode=True, sort_keys=False)


def print_report(report: Dict[str, Any]) -> None:
    """Print formatted console summary."""
    ep = report['episode_id']
    status = report['overall_status']
    print(f"\n{'=' * 60}")
    print(f"TTS VALIDATION: {ep}  [{status}]")
    print(f"{'=' * 60}")
    print(f"VO Lines: {report['total_vo_lines']}")
    print(f"Schema:   {', '.join(report['schema_columns'])}")
    print()

    for rule_name, result in report['rule_results'].items():
        icon = '✅' if result['status'] == 'PASS' else '❌'
        print(f"  {icon} {rule_name}: {result['status']}")

        if rule_name == 'RULE_TTS_SCRIPTURE_SPELLING' and result['violation_count'] > 0:
            print(f"     → {result['violation_count']} lines with colon-notation")
            for v in result['details'][:3]:
                print(f"       Line {v['line']}: {v['matches']} — \"{v['text_snippet']}...\"")
            if result['violation_count'] > 3:
                print(f"       ... and {result['violation_count'] - 3} more")

        elif rule_name == 'RULE_TTS_MIN_WORDS' and result['violation_count'] > 0:
            print(f"     → {result['violation_count']} lines with < 2 words")
            for v in result['details'][:5]:
                print(f"       Line {v['line']}: \"{v['text']}\" ({v['word_count']} words)")

        elif rule_name == 'RULE_ES_TRANSLATION':
            if not result['has_vo_es_column']:
                print(f"     → VO_ES column missing from schema")
            elif result['empty_vo_es_count'] > 0:
                print(f"     → {result['empty_vo_es_count']} lines with empty VO_ES")

    print(f"{'=' * 60}\n")


def find_all_episodes(base_dir: Path) -> List[Path]:
    """Find all episode directories containing vo_script_table.csv."""
    episodes_dir = base_dir / "episodes"
    if not episodes_dir.exists():
        return []
    results = []
    for ep_dir in sorted(episodes_dir.iterdir()):
        if ep_dir.is_dir() and (ep_dir / "vo_script_table.csv").exists():
            results.append(ep_dir)
    return results


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python tts_validator.py <episode_dir>")
        print("       python tts_validator.py --all")
        print("\nExamples:")
        print("  python tts_validator.py episodes/EC_0001")
        print("  python tts_validator.py --all")
        sys.exit(1)

    # Determine project root (scripts/ is one level below root)
    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent

    if sys.argv[1] == '--all':
        episode_dirs = find_all_episodes(project_root)
        if not episode_dirs:
            print("No episodes with vo_script_table.csv found.")
            sys.exit(1)

        print(f"\nBatch validating {len(episode_dirs)} episodes...\n")
        all_reports = []
        pass_count = 0
        fail_count = 0

        for ep_dir in episode_dirs:
            try:
                report = validate_episode(ep_dir)
                all_reports.append(report)
                print_report(report)

                # Save individual report
                output_path = ep_dir / "tts_report.yaml"
                save_report(report, output_path)

                if report['overall_status'] == 'PASS':
                    pass_count += 1
                else:
                    fail_count += 1

            except Exception as e:
                print(f"Error processing {ep_dir.name}: {e}")
                fail_count += 1

        # Batch summary
        print(f"\n{'=' * 60}")
        print(f"BATCH SUMMARY")
        print(f"{'=' * 60}")
        print(f"Total: {len(episode_dirs)} | Pass: {pass_count} | Fail: {fail_count}")
        print(f"{'=' * 60}\n")

        sys.exit(0 if fail_count == 0 else 1)
    else:
        episode_dir = Path(sys.argv[1])
        if not episode_dir.is_absolute():
            episode_dir = project_root / episode_dir

        if not episode_dir.exists():
            print(f"Error: Directory not found: {episode_dir}")
            sys.exit(1)

        try:
            report = validate_episode(episode_dir)
            print_report(report)

            output_path = episode_dir / "tts_report.yaml"
            save_report(report, output_path)
            print(f"Report saved to: {output_path}")

            sys.exit(0 if report['overall_status'] == 'PASS' else 1)

        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)


if __name__ == "__main__":
    main()
