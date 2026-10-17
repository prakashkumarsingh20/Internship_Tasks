# Problem: Collections.Counter()
# HackerRank: https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

if __name__ == '__main__':
    X = int(input())
    shoe_sizes = Counter(map(int, input().split()))

    N = int(input())
    total_earnings = 0

    for _ in range(N):
        size, price = map(int, input().split())

        if shoe_sizes[size] > 0:
            total_earnings += price
            shoe_sizes[size] -= 1

    print(total_earnings)
