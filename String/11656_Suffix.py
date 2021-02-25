import sys
input = sys.stdin.readline

S =input().rstrip()

S_list = []

for i in range(len(S)):
    S_list.append(S)
    S=S[1:]
S_list.sort()

for i in S_list:
    print(i)
