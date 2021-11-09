import sys
input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(31)]
dp[1]=0
dp[2]=3
for i in range(4, 31, 2):
    dp[i] = dp[2] * dp[i - 2] #지금까지 추가한거에 길이 2 짜리 추가
    for j in range(4, i, 2):
        dp[i] += dp[i-j]*2 #dp[i-j] * j에서의 새로운 블럭(2)
    dp[i]+=2 #i의 새로운 블럭

print(dp[n])
