# Problem: Weighted Uniform Strings
# Link: https://www.hackerrank.com/challenges/weighted-uniform-string/problem

import math
import os
import random
import re
import sys


def weightedUniformStrings(s, queries):
    weights = set()
    i = 0
    n = len(s)

    while i < n:
        j = i
        w = ord(s[i]) - ord('a') + 1
        while j < n and s[j] == s[i]:
            j += 1
            weights.add(w * (j - i))
        i = j

    result = []
    for x in queries:
        result.append("Yes" if x in weights else "No")
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
