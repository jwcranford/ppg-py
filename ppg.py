#!/usr/bin/env python3

import secrets
import sys
import argparse
import math

DEFAULT_ENTROPY_TARGET = 75

parser = argparse.ArgumentParser(description='ppg.py is a command-line tool to generate passphrases.',
    epilog='''By default, the number of words in each passphrase depends on the size 
of the input file. For example:
    # of words in file   # of words in passphrase
    ------------------   ------------------------
                1024                          8
                2048                          7
                4096                          7
                8192                          6''',
    formatter_class=argparse.RawDescriptionHelpFormatter
    )
parser.add_argument("file", help='word list, one word per line. See diceware8k.txt for an example')
parser.add_argument("-w", "--word_count", 
    help="number of words in the passphrase",
    default=-1,
    type=int)
parser.add_argument("-n", "--phrase_count",
    help="number of passphrases to generate (default is 1)",
    default=1,
    type=int)
parser.add_argument("-d", "--digit",
    help="adds a single digit at a random place in the passphrase",
    action="store_true")
parser.add_argument("-s", '--special',
    help='adds a single special character at a random place in the passphrase',
    action="store_true")

args = parser.parse_args()

with open(args.file) as f:
    words = [word.strip() for word in f]

size = len(words)
entropy_per_word = math.log(size, 2)
even_size = 1 << int(entropy_per_word)
even_words = words[:even_size]

# assign word_count based on size of file
word_count = args.word_count
if word_count == -1:
    word_count = math.ceil(DEFAULT_ENTROPY_TARGET/entropy_per_word)

# Use digits 2-9 for random digits, where needed. We avoid 0 and 1 to 
# avoid confusion with o and l.
digits = ['2', '3', '4', '5', '6', '7', '8', '9']

special = ['!', '@', '#', '$', '.', '^', '*', '/']

for n in range(args.phrase_count):
    phrase = [secrets.choice(even_words) for i in range(word_count)]
    if (args.digit):
        location = secrets.choice(range(0, len(phrase) + 1))
        phrase.insert(location, secrets.choice(digits))
    if (args.special):
        location = secrets.choice(range(0, len(phrase) + 1))
        phrase.insert(location, secrets.choice(special))
    print(' '.join(phrase)) 
