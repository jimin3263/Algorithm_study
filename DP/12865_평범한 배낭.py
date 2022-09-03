import sys

input = sys.stdin.readline

n, k = map(int, input().split())  # n개, 최종무게 k
arr = [[0,0]]
for i in range(n):
    w, v = map(int, input().split())
    arr.append([w, v])  # 가치 (v)의 최댓값을 구하라

dp = list([0] * (k + 1) for _ in range(n + 1))  #무게, 개수
for i in range(1, n+1): #개수
    w, v = arr[i][0], arr[i][1]
    for j in range(1, k+1): #무게
        if j < w:
            dp[i][j] = dp[i-1][j]
        elif j >= w: #다른거와 합쳐야함
            dp[i][j] = max(dp[i-1][j-w]+v, dp[i-1][j])
print(dp[n][k])
