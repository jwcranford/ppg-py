#!/usr/bin/env python3

import secrets
import sys

if (len(sys.argv) < 2):
    print(f"Usage: {sys.argv[0]} file")
    print("    where file is a word list, one word per line")
    sys.exit(1)

word_file = sys.argv[1]
password = ''
with open(word_file) as f:
    words = [word.strip() for word in f]
    password += ' '.join(secrets.choice(words) for i in range(5))
print(password)
