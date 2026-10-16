# Problem 14: Set .add()
# HackerRank: https://www.hackerrank.com/challenges/py-set-add/problem

n = int(input())

countries = set()

for _ in range(n):
    country = input()
    countries.add(country)

print(len(countries))
