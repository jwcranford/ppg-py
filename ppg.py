#!/usr/bin/env python3

import secrets
import sys

# On standard Linux systems, use a convenient dictionary file.
# Other platforms may need to provide their own word-list.
password = ''
with open(sys.argv[1]) as f:
    words = [word.strip() for word in f]
    password += ' '.join(secrets.choice(words) for i in range(5))
print(password)
