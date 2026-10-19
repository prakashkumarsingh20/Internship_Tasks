# Problem: Set .symmetric_difference() Operation
# HackerRank: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

n = int(input())
english = set(map(int, input().split()))

m = int(input())
french = set(map(int, input().split()))

result = english.symmetric_difference(french)

print(len(result))
