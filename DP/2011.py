import sys
input = sys.stdin.readline

arr=list(map(int,input().strip()))
n = len(arr)
dp = [0] * (n+1)

dp[0] = 1
dp[1] = 1

if (arr[0] == 0) : # 예외
    print("0")
else:
    arr = [0] + arr
    for i in range(2, n+1):
        if (arr[i]> 0):
            dp[i] += dp[i - 1] #한 자리 가능할 때
        temp = arr[i-1]*10 + arr[i]
        if (temp >= 10 and temp <= 26): #두 자리 가능할 때
            dp[i] += dp[i-2]

    print(dp[n]%1000000)
