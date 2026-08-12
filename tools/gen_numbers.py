#!/usr/bin/env python3

# gen_numbers.py

# Generates 23 random numbers from 0 to 1999.
# Its purpose is to test artisan_random.py
# It should not be used for real wallet generation.

import secrets

for i in range(23):
    print("{0:04d}".format(secrets.randbelow(2000)))
