# Problem: Tuples
# Link: https://www.hackerrank.com/challenges/python-tuples/problem

def tuple_hash(t):
    # Old (pre-Python 3.8) tuple hash algorithm, 64-bit
    M = (1 << 64) - 1
    x = 0x345678
    mult = 1000003
    length = len(t)
    for item in t:
        length -= 1
        y = hash(item) & M
        x = ((x ^ y) * mult) & M
        mult = (mult + 82520 + length + length) & M
    x = (x + 97531) & M
    if x >= (1 << 63):
        x -= (1 << 64)
    if x == -1:
        x = -2
    return x

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(tuple_hash(t))
