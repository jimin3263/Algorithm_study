#가장 큰 증가하는 수열
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [arr[i] for i in range(n)]

for i in range(1,n):
    for j in range(i):
        if arr[i] > arr[j]: #현재 숫자보다 작은수 찾는다.
            dp[i] = max(dp[j]+arr[i], dp[i]) #현재 수 + 비교 중인 작은 수의 누적 합, 현재 수의 누적 합 중 큰 값 저장
print(max(dp))
