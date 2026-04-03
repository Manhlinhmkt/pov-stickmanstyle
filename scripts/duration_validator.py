#!/usr/bin/env python
"""
Duration Validator for Biblical Wisdom Episodes
Counts words per beat and estimates duration based on WPM.
Outputs adjustment instructions for LLM.
"""

import csv
import yaml
import sys
from pathlib import Path
from typing import Dict, List, Any


def count_words(text: str) -> int:
    """Count words in a string."""
    if not text:
        return 0
    return len(text.split())


def load_csv(filepath: Path) -> List[Dict[str, str]]:
    """Load CSV file into list of dicts."""
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        return list(reader)


def load_yaml(filepath: Path) -> Dict[str, Any]:
    """Load YAML file."""
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        return yaml.safe_load(f)


def calculate_duration(words: int, wpm: int = 140) -> float:
    """Calculate duration in seconds from word count."""
    return (words / wpm) * 60


def estimate_sentence_adjustment(variance_pct: float, avg_words_per_sentence: int = 12) -> int:
    """
    Estimate how many sentences to add/remove.
    Positive = add sentences, Negative = remove sentences.
    """
    # Rough calculation: if we're 20% under, we need to add ~20% more content
    # Convert to sentence count based on average sentence length
    if abs(variance_pct) < 15:
        return 0
    
    # Estimate target adjustment in words, then convert to sentences
    # This is intentionally rough - LLM will use judgment
    sentence_change = int(variance_pct / 10)  # ~1 sentence per 10% variance
    return sentence_change


def validate_episode(episode_dir: Path) -> Dict[str, Any]:
    """
    Validate duration for an episode.
    
    Args:
        episode_dir: Path to episode directory (e.g., episodes/EC_0001)
        
    Returns:
        Validation report as dict
    """
    # Load files
    vo_draft_path = episode_dir / "vo_draft_table.csv"
    l2_breakdown_path = episode_dir / "l2_breakdown_table.csv"
    metadata_path = episode_dir / "metadata.yaml"
    
    if not vo_draft_path.exists():
        raise FileNotFoundError(f"VO draft not found: {vo_draft_path}")
    if not l2_breakdown_path.exists():
        raise FileNotFoundError(f"L2 breakdown not found: {l2_breakdown_path}")
    if not metadata_path.exists():
        raise FileNotFoundError(f"Metadata not found: {metadata_path}")
    
    vo_draft = load_csv(vo_draft_path)
    l2_breakdown = load_csv(l2_breakdown_path)
    metadata = load_yaml(metadata_path)
    
    # Get target duration from metadata
    # Note: duration_profile is a string, actual values are at root level
    target_duration_sec = metadata.get('estimated_duration_sec', 900)
    wpm_value = metadata.get('wpm')
    if wpm_value is None:
        vp = metadata.get('voice_profile', {})
        if isinstance(vp, dict):
            wpm_value = vp.get('avg_reading_speed_wpm', 140)
        else:
            wpm_value = 140
    wpm = wpm_value

    target_words_total = metadata.get('estimated_word_count', int(target_duration_sec * wpm / 60))
    
    # Build target word count per beat from L2
    beat_targets = {}
    for row in l2_breakdown:
        beat_id = row.get('Beat_ID', '')
        target = row.get('Target_Word_Count', '0')
        try:
            beat_targets[beat_id] = int(target)
        except ValueError:
            beat_targets[beat_id] = 0
    
    # Calculate actual words per beat from VO draft
    beat_actuals = {}
    for row in vo_draft:
        beat_id = row.get('Ref_Beat', '')
        text = row.get('Draft_Text_EN', '')
        words = count_words(text)
        
        if beat_id not in beat_actuals:
            beat_actuals[beat_id] = 0
        beat_actuals[beat_id] += words
    
    # Analyze each beat
    beat_analysis = []
    total_actual_words = 0
    total_target_words = 0
    
    for beat_id in sorted(set(list(beat_targets.keys()) + list(beat_actuals.keys()))):
        target = beat_targets.get(beat_id, 0)
        actual = beat_actuals.get(beat_id, 0)
        total_actual_words += actual
        total_target_words += target
        
        if target == 0:
            variance_pct = 0
        else:
            variance_pct = ((actual - target) / target) * 100
        
        # Determine action
        if variance_pct < -15:
            action = "EXPAND"
            sentence_adj = estimate_sentence_adjustment(variance_pct)
            instruction = f"Add {abs(sentence_adj)}-{abs(sentence_adj)+1} sentences to deepen content"
        elif variance_pct > 15:
            action = "TRIM"
            sentence_adj = estimate_sentence_adjustment(variance_pct)
            instruction = f"Remove {abs(sentence_adj)}-{abs(sentence_adj)+1} sentences while preserving core message"
        else:
            action = "OK"
            instruction = ""
        
        beat_analysis.append({
            'beat_id': beat_id,
            'target_words': target,
            'actual_words': actual,
            'variance_pct': round(variance_pct, 1),
            'action': action,
            'instruction': instruction
        })
    
    # Calculate totals
    if total_target_words == 0:
        total_variance_pct = 0
    else:
        total_variance_pct = ((total_actual_words - total_target_words) / total_target_words) * 100
    
    actual_duration_sec = calculate_duration(total_actual_words, wpm)
    
    # Determine overall status
    if abs(total_variance_pct) <= 15:
        status = "PASS"
    else:
        status = "NEEDS_ADJUSTMENT"
    
    # Count actions
    beats_ok = sum(1 for b in beat_analysis if b['action'] == 'OK')
    beats_expand = sum(1 for b in beat_analysis if b['action'] == 'EXPAND')
    beats_trim = sum(1 for b in beat_analysis if b['action'] == 'TRIM')
    
    report = {
        'episode_id': metadata.get('episode_id', 'UNKNOWN'),
        'target_duration_sec': target_duration_sec,
        'actual_duration_sec': round(actual_duration_sec, 1),
        'target_words': total_target_words,
        'actual_words': total_actual_words,
        'variance_pct': round(total_variance_pct, 1),
        'status': status,
        'wpm': wpm,
        'summary': {
            'beats_ok': beats_ok,
            'beats_expand': beats_expand,
            'beats_trim': beats_trim
        },
        'beat_analysis': beat_analysis
    }
    
    return report


def save_report(report: Dict[str, Any], output_path: Path) -> None:
    """Save report as YAML."""
    with open(output_path, 'w', encoding='utf-8-sig') as f:
        yaml.dump(report, f, default_flow_style=False, allow_unicode=True, sort_keys=False)


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python duration_validator.py <episode_dir>")
        print("Example: python duration_validator.py episodes/EC_0001")
        sys.exit(1)
    
    episode_dir = Path(sys.argv[1])
    
    if not episode_dir.exists():
        print(f"Error: Directory not found: {episode_dir}")
        sys.exit(1)
    
    try:
        report = validate_episode(episode_dir)
        
        # Save report
        output_path = episode_dir / "duration_report.yaml"
        save_report(report, output_path)
        
        # Print summary
        print(f"\n{'='*60}")
        print(f"DURATION VALIDATION REPORT: {report['episode_id']}")
        print(f"{'='*60}")
        print(f"Target Duration: {report['target_duration_sec']} sec ({report['target_words']} words)")
        print(f"Actual Duration: {report['actual_duration_sec']} sec ({report['actual_words']} words)")
        print(f"Variance: {report['variance_pct']:+.1f}%")
        print(f"Status: {report['status']}")
        print(f"\nBeat Summary:")
        print(f"  - OK: {report['summary']['beats_ok']}")
        print(f"  - Need EXPAND: {report['summary']['beats_expand']}")
        print(f"  - Need TRIM: {report['summary']['beats_trim']}")
        print(f"\nReport saved to: {output_path}")
        print(f"{'='*60}\n")
        
        # Exit code based on status
        sys.exit(0 if report['status'] == 'PASS' else 1)
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
