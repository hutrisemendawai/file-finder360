import argparse
import os
import fnmatch
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('--disk', required=True, help='Disk letter, e.g. C')
parser.add_argument('--name', required=True, help='Filename or pattern to search for, e.g. *.txt')
args = parser.parse_args()

root = f"{args.disk}:\\"
for dirpath, _, files in os.walk(root, onerror=lambda e: None):
    for f in files:
        if fnmatch.fnmatch(f, args.name):
            print(Path(dirpath) / f)
