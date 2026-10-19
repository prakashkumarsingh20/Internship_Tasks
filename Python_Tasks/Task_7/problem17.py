# Problem: Separate the Numbers
# Link: https://www.hackerrank.com/challenges/separate-the-numbers/problem

def separateNumbers(s):
    if s[0] == '0':
        print("NO")
        return

    for i in range(1, len(s) // 2 + 1):
        first = int(s[:i])
        built = str(first)
        num = first

        while len(built) < len(s):
            num += 1
            built += str(num)

        if built == s:
            print("YES", first)
            return

    print("NO")

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
