# Problem: Set Mutations
# Link: https://www.hackerrank.com/challenges/py-set-mutations/problem

n = int(input())
a = set(map(int, input().split()))
m = int(input())

for _ in range(m):
    operation, length = input().split()
    other = set(map(int, input().split()))
    getattr(a, operation)(other)

print(sum(a))
