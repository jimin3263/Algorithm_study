import sys, re
input = sys.stdin.readline

t = re.compile('(^[ABCDEF]?A+F+C+[ABCDEF]?$)')
T = int(input())
for i in range(T):
    str = input()
    if t.match(str):
        print("Infected!")
    else:
        print("Good")