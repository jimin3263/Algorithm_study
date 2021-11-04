#포도주
#연속 2잔까지만 허용
import sys
input = sys.stdin.readline

n = int(input())

arr=[0]
for i in range(n):
    arr.append(int(input()))

dp = [0]
dp.append(arr[1])

if n>1 : #조건 달지 않으면 인덱스 오류 발생...(1 ≤ n ≤ 10,000) 조건 잘 보기!
    dp.append(arr[1]+arr[2]) #2잔까지만 있다고 할때 최댓값

for i in range(3,n+1):
    #3연속을 피하면서 수행할 수 있는 경우의 수 세가지 존재
    dp.append(max(dp[i-1], arr[i]+arr[i-1]+dp[i-3] , dp[i-2]+arr[i]))

print(dp[n])
