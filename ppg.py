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

# def usage():
#     print(f"{sys.argv[0]} generates a passphrase from the given file of the")
#     print('given number of words.')
#     print()
#     print(f"Usage: {sys.argv[0]} [-w word_count] file")
#     print("where")
#     print('  file           is a word list, one word per line')
#     print('  word_count     is the number of words in the passphrase ')
#     print('                 (default value: 5)')

# if (len(sys.argv) < 2):
#     usage()
#     sys.exit(1)

args = parser.parse_args()

# argi = 1
# word_count = 5
# if (len(sys.argv) <= 4 and '-w' == sys.argv[argi]):
#     argi += 1
#     try:
#         word_count = int(sys.argv[argi])
#     except ValueError:
#         print(f"Invalid word count: {sys.argv[argi]}")
#         print()
#         usage()
#         sys.exit(2)
#     argi += 1


# word_file = sys.argv[argi]

with open(args.file) as f:
    words = [word.strip() for word in f]

password = ' '.join(secrets.choice(words) for i in range(args.word_count))
print(password)
