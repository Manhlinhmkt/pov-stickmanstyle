#!/usr/bin/env python3
"""Re-encode CSV files to UTF-8 BOM for Excel compatibility."""
import sys, glob, os

ep_dir = sys.argv[1] if len(sys.argv) > 1 else "episodes/EC_0001"
csvs = glob.glob(os.path.join(ep_dir, "*.csv"))

for f in csvs:
    with open(f, "r", encoding="utf-8") as fh:
        content = fh.read()
    # Remove existing BOM if any, then write with BOM
    content = content.lstrip("\ufeff")
    with open(f, "w", encoding="utf-8-sig", newline="") as fh:
        fh.write(content)
    print(f"✅ {os.path.basename(f)}")

print(f"\nDone: {len(csvs)} files re-encoded with UTF-8 BOM")
