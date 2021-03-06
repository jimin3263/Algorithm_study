import sys
import math
input = sys.stdin.readline

def DP ():
    K = int(input())
    arr = list(map(int, input().split()))
    min_arr = list([0] * K for _ in range(K))
    # 주대각선 바로 위에만 비교
    for j in range(1,K):
        for i in range(j-1,-1,-1):
            small = math.inf
            for k in range(j-i):
                small= min(small,min_arr[i][i+k]+min_arr[i+k+1][j])
            min_arr[i][j] = small + sum(arr[i:j+1])

    print(min_arr[0][K-1])
T = int(input())
for i in range(T):
    DP()
