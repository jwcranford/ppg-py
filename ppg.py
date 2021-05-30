#!/usr/bin/env python3

import secrets
import sys
import argparse
import math

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
parser.add_argument("-d", "--digit",
    help="adds a single digit at a random place between the words of the passphrase",
    action="store_true")

args = parser.parse_args()

with open(args.file) as f:
    words = [word.strip() for word in f]

size = len(words)
entropy_per_word = math.log(size, 2)
even_size = 1 << int(entropy_per_word)
even_words = words[:even_size]

# Use digits 2-9 for random digits, where needed. We avoid 0 and 1 to 
# avoid confusion with o and l.
digits = ['2', '3', '4', '5', '6', '7', '8', '9']

for n in range(args.phrase_count):
    phrase = [secrets.choice(even_words) for i in range(args.word_count)]
    if (args.digit):
        location = secrets.choice(range(0, len(phrase) + 1))
        phrase.insert(location, secrets.choice(digits))
    print(' '.join(phrase)) 
