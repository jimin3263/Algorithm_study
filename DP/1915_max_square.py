import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [list(map(int,input().strip())) for _ in range(n)]
arr2 = [[0]*(m+1) for _ in range(n+1)]

max_size = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if arr[i-1][j-1]==1:
            #정사각형 확인 : 좌 위 대각선위 확인
            arr2[i][j] = min(arr2[i][j-1],arr2[i-1][j],arr2[i-1][j-1])+1
            if arr2[i][j]>max_size:
                max_size = arr2[i][j]

print(max_size**2)
