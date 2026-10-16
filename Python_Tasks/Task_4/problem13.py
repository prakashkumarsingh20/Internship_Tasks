# Problem 13: Symmetric Difference
# HackerRank: https://www.hackerrank.com/challenges/symmetric-difference/problem

M = int(input())
set_a = set(map(int, input().split()))

N = int(input())
set_b = set(map(int, input().split()))

result = sorted(set_a.symmetric_difference(set_b))

for num in result:
    print(num)
