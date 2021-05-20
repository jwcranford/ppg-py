#!/usr/bin/env python3

import secrets
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", help='word list, one word per line')
parser.add_argument("-w", "--word_count", 
    help="number of words in the passphrase (default is 5)",
    default=5,
    type=int)
parser.add_argument("-n", "--phrase_count",
    help="number of passphrases to generate (default is 20)",
    default=20,
    type=int)

args = parser.parse_args()

with open(args.file) as f:
    words = [word.strip() for word in f]

for n in range(args.phrase_count):
    print(' '.join(secrets.choice(words) for i in range(args.word_count))) 
