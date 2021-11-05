#가장 긴 증가하는 수열
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(1,n):
    for j in range(i):
        if arr[i] > arr[j]: #현재 숫자보다 작은수 체크
            dp[i] = max(dp[j]+1, dp[i]) #현재 비교하는 수 j의 길이 dp[j]+1 (arr[i]), 비교하면서 저장한 값 dp[i] 중 큰 값 저장
print(max(dp))
