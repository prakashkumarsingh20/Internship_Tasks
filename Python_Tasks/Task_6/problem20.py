# Problem: Validating phone numbers
# Link: https://www.hackerrank.com/challenges/validating-the-phone-number/problem

import re

n = int(input())

for _ in range(n):
    number = input()
    if re.fullmatch(r"[789][0-9]{9}", number):
        print("YES")
    else:
        print("NO")
