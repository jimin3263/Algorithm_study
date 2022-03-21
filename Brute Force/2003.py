#2003
n, m = map(int, input().split())
arr = list(map(int,input().split()))
#n개의 수열, i번째부터 j번빼 수의 합이 M이 되는 경우의 수
#시작 지점을 하나씩 다 해보면 되는거 아닌가..

count = 0
for i in range(n):
    result = 0
    for j in range(i,n):
        result += arr[j]
        if (result == m):
            count += 1

print(count)
