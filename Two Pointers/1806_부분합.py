import math
import sys
input = sys.stdin.readline

#가장 작은 길이 리턴
n, s = map(int,input().split()) #길이 n, 부분합 s이상이 되는 것 중
arr = list(map(int,input().split()))

i, j = 0, 0
temp = arr[0]
answer = math.inf

while True:
    if temp >= s: #크다면 왼쪽 증가
        temp -= arr[i]
        answer = min(answer, j-i+1)
        i += 1
    else: #작다면 오른쪽 증가
        j += 1
        if j == n:
            break
        temp += arr[j]
print(0 if answer == math.inf else answer)

