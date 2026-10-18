# Problem: Check Subset
# Link: https://www.hackerrank.com/challenges/py-check-subset/problem

t = int(input())

for _ in range(t):
    a = int(input())
    set_a = set(map(int, input().split()))
    b = int(input())
    set_b = set(map(int, input().split()))
    print(set_a.issubset(set_b))
