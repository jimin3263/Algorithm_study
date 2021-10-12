# 인접한 숫자는 1만 차이 날 수 있음
import sys
input = sys.stdin.readline
n = int(input())

dp = [[0]*10 for _ in range(n+1)]
for i in range(10):
    dp[1][i] = 1 #1로 일단 다 채우기 (숫자 1개일때는 하나로)

for i in range(2, n+1): #길이가 2일때
    for j in range(10):
        if(j == 9):
            dp[i][j] = dp[i-1][j-1] #9인 경우 8만 올 수 있음
        elif(j == 0):
            dp[i][j] = dp[i-1][j+1] #0인 경우 1만 올 수 있음
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1] #나머지는 2개씩 가능


print(sum(dp[n][1:10])%1000000000)#0부터 시작하는 숫자는 뺌 -> 1부터 합
