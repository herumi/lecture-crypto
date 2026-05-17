#!/usr/bin/env python3
"""Update 'last update: YYYY/MM/DD' in markdown files with the file's modification date."""

import re
import sys
import os
from datetime import datetime
from pathlib import Path


PATTERN = re.compile(r'last update:\s*(\d{4}/\d{2}/\d{2})', re.IGNORECASE)


def update_file(path: Path) -> bool:
    stat = path.stat()
    mtime = datetime.fromtimestamp(stat.st_mtime).date()

    content = path.read_text(encoding='utf-8')
    m = PATTERN.search(content)

    if not m:
        print(f"  skip: {path} (no 'last update' found)")
        return False

    current_date = datetime.strptime(m.group(1), '%Y/%m/%d').date()

    if mtime <= current_date:
        print(f"  up-to-date: {path}")
        return False

    new_date_str = f"last update: {mtime.strftime('%Y/%m/%d')}"
    new_content = PATTERN.sub(new_date_str, content)

    path.write_text(new_content, encoding='utf-8')
    os.utime(path, (stat.st_atime, stat.st_mtime))
    print(f"  updated: {path}  -> {mtime.strftime('%Y/%m/%d')}")
    return True


def main():
    targets = sys.argv[1:]

    if targets:
        paths = [Path(t) for t in targets]
    else:
        paths = sorted(Path('.').glob('*.md'))

    updated = 0
    for path in paths:
        if not path.is_file():
            print(f"  not found: {path}")
            continue
        if updated_file := update_file(path):
            updated += 1

    print(f"\n{updated} file(s) updated.")


if __name__ == '__main__':
    main()
