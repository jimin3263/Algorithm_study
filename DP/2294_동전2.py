import math
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

dp = [math.inf] * (k+1)
dp[0] = 0

for i in range(n):
    for j in range(arr[i], k+1):
        dp[j] = min(dp[j], dp[j-arr[i]] + 1)

if dp[-1] == math.inf:
    print(-1)
else:
    print(dp[-1])