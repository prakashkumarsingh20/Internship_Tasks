# Problem: Alphabet Rangoli
# Link: https://www.hackerrank.com/challenges/alphabet-rangoli/problem

import string

def print_rangoli(size):
    alpha = string.ascii_lowercase
    width = 4 * size - 3
    lines = []

    for i in range(size):
        left = alpha[size - 1 - i:size][::-1]
        right = left[::-1][1:]
        row = "-".join(left + right)
        lines.append(row.center(width, '-'))

    for line in lines + lines[-2::-1]:
        print(line)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
