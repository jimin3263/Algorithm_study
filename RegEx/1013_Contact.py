import re
import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    str = input().rstrip()
    print(re.match('(100+1+|01)+', str))

    if re.match('(100+1+|01)+', str):
        print("YES")
    else:
        print("NO")