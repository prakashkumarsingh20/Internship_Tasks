# Problem: Game of Thrones - I
# Link: https://www.hackerrank.com/challenges/game-of-thrones/problem

import os
from collections import Counter

def gameOfThrones(s):
    counts = Counter(s)
    odd = 0
    for ch in counts:
        if counts[ch] % 2 != 0:
            odd += 1
    if odd <= 1:
        return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
