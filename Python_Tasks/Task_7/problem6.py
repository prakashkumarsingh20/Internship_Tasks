# Problem: Pangrams
# Link: https://www.hackerrank.com/challenges/pangrams/problem

import math
import os
import random
import re
import sys

def pangrams(s):
    letters = set(ch for ch in s.lower() if ch.isalpha())
    if len(letters) == 26:
        return "pangram"
    return "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
