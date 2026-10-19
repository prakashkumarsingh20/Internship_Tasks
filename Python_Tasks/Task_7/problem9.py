# Problem: Beautiful Binary String
# Link: https://www.hackerrank.com/challenges/beautiful-binary-string/problem

import math
import os
import random
import re
import sys

def beautifulBinaryString(b):
    return b.count("010")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
