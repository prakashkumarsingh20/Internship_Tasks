# Problem: Anagram
# Link: https://www.hackerrank.com/challenges/anagram/problem

import os
from collections import Counter

def anagram(s):
    n = len(s)
    if n % 2 != 0:
        return -1

    a = Counter(s[:n // 2])
    b = Counter(s[n // 2:])

    changes = 0
    for ch in a:
        if a[ch] > b[ch]:
            changes += a[ch] - b[ch]
    return changes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
