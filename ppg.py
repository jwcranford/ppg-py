#!/usr/bin/env python3

import secrets
import sys

def usage():
    print(f"{sys.argv[0]} generates a passphrase from the given file of the")
    print('given number of words.')
    print()
    print(f"Usage: {sys.argv[0]} [-w word_count] file")
    print("where")
    print('  file           is a word list, one word per line')
    print('  word_count     is the number of words in the passphrase ')
    print('                 (default value: 5)')

if (len(sys.argv) < 2):
    usage()
    sys.exit(1)

argi = 1
word_count = 5
if (len(sys.argv) <= 4 and '-w' == sys.argv[argi]):
    argi += 1
    try:
        word_count = int(sys.argv[argi])
    except ValueError:
        print(f"Invalid word count: {sys.argv[argi]}")
        print()
        usage()
        sys.exit(2)
    argi += 1

word_file = sys.argv[argi]

with open(word_file) as f:
    words = [word.strip() for word in f]

password = ' '.join(secrets.choice(words) for i in range(word_count))
print(password)
