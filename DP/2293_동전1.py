import sys
input = sys.stdin.readline

n, k = map(int, input().split()) #n가지 종류, k원
coins = []
for i in range(n):
    coin = int(input())
    coins.append(coin)
dp = [0] * (k+1)
dp[0] = 1

for coin in coins:
    for j in range(coin, k+1):
        if j-coin >= 0:
            dp[j] += dp[j-coin]
    print(dp)

print(dp[-1])