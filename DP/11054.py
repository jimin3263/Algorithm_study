#11054
#바이토닉 수열: 특정 수까지는 증가, 특정 수 까지는 감소

n = int(input())
arr = list(map(int, input().split()))

inc_dp = [1 for i in range(n)]
dec_dp = [1 for i in range(n)]

#증가
for i in range(n):
    for j in range(i):
        if (arr[j] < arr[i]):
            inc_dp[i] = max(inc_dp[j]+1 , inc_dp[i])
#감소
for i in range(n-1, -1, -1):
    for j in range(n-1,i-1,-1):
        if (arr[j] < arr[i]):
            dec_dp[i] = max(dec_dp[j]+1 , dec_dp[i])

#증가 감소 배열의 합 구함
result = []
for i in range(n):
    result.append(inc_dp[i] + dec_dp[i])

print(max(result) - 1) #해당 숫자가 중복되므로 1 빼줌  
