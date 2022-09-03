import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n
for i in range(1, n): #10 20 10 30 20 50 / 1 2 1
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[j]+1, dp[i])
answer = []

#저장된 내용 바탕으로 수열 출력
max_dp = max(dp)
for i in range(n-1, -1, -1):
    if max_dp == dp[i]:
        answer.append(arr[i])
        max_dp -= 1

print(max(dp))
print(*answer[::-1])