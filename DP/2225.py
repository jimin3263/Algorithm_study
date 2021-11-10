import sys
input = sys.stdin.readline

n, k = map(int,input().split())
arr = [[0]*201 for _ in range(201)]

#초기화
for i in range(201):
    arr[1][i]=1
    arr[2][i]=i+1
    arr[i][1]=i

for i in range(2,201): #i: 더한 횟수
    for j in range(2, 201): #j: 총합
        arr[i][j] = arr[i-1][j] + arr[i][j-1]

print(arr[k][n]% 1000000000) #조건 잘보기
