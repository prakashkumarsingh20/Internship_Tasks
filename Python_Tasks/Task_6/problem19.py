# Problem: Company Logo
# Link: https://www.hackerrank.com/challenges/most-commons/problem

from collections import Counter

if __name__ == '__main__':
    s = input()
    counts = Counter(s)
    top3 = sorted(counts.items(), key=lambda x: (-x[1], x[0]))[:3]
    for char, count in top3:
        print(char, count)
