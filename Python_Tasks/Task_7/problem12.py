# Problem: Making Anagrams
# Link: https://www.hackerrank.com/challenges/making-anagrams/problem

import os
from collections import Counter

def makingAnagrams(s1, s2):
    c1 = Counter(s1)
    c2 = Counter(s2)
    deletions = 0
    for ch in set(c1) | set(c2):
        deletions += abs(c1[ch] - c2[ch])
    return deletions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
