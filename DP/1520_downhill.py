import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

M,N = map(int, input().split())
arr =[list(map(int,input().split())) for _ in range(M)]
count = [[-1]*N for _ in range(M)]
x_list = [-1,1,0,0]
y_list = [0,0,-1,1]

def DP (x,y):
    if count[y][x] != -1:
        return count[y][x]
    if (x == (N - 1) and y == (M - 1)):
        return 1
    count[y][x]=0
    for i in range(4):
        go_x=x+ x_list[i]
        go_y=y+ y_list[i]
        if (0<=go_x<N and 0<=go_y<M):
            if (arr[y][x]>arr[go_y][go_x]):

                count[y][x]+=DP(go_x,go_y)
    return count[y][x]

print(DP(0,0))
