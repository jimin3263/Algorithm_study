import sys
input = sys.stdin.readline

#계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
#연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
#마지막 도착 계단은 반드시 밟아야 한다.

n = int(input())
arr = [0 for i in range(301)]
for i in range(n):
    arr[i] = int(input())

#3연속 피하기, i를 포함해야 함 -> arr[i]+arr[i-1]+dp[i-3] , dp[i-2]+arr[i]

dp = [0 for i in range(301)]
dp[0] = arr[0]
dp[1] = arr[0] + arr[1]
dp[2] = max(arr[0] + arr[2], arr[1]+arr[2])

for i in range(3, n):
    dp[i] = max(arr[i]+arr[i-1]+dp[i-3] , dp[i-2]+arr[i])

print(dp[n-1])
