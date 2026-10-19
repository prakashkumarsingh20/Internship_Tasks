# Problem: Sherlock and the Valid String
# Link: https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

import os
from collections import Counter

def isValid(s):
    char_count = Counter(s)
    freq_count = Counter(char_count.values())

    if len(freq_count) == 1:
        return "YES"

    if len(freq_count) > 2:
        return "NO"

    (f1, c1), (f2, c2) = sorted(freq_count.items())

    if f1 == 1 and c1 == 1:
        return "YES"

    if f2 - f1 == 1 and c2 == 1:
        return "YES"

    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
