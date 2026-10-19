# Problem: Mars Exploration
# Link: https://www.hackerrank.com/challenges/mars-exploration/problem

def marsExploration(s):
    expected = "SOS"
    changed = 0
    for i in range(len(s)):
        if s[i] != expected[i % 3]:
            changed += 1
    return changed

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
