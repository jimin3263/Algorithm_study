#4963
import sys
input = sys.stdin.readline

dx = [0,0,-1,1,1,-1,1,-1] #상,하,좌,우,대각선
dy = [1,-1,0,0,1,-1,-1,1]

def bfs(y,x):
    queue = [(y,x)]
    arr[y][x] = 0 #방문 표시

    global count
    while (queue):
        y,x = queue.pop()
        for i in range(8):
            ny,nx = y+dy[i], x+dx[i]
            if(0<=ny and ny< h and 0<=nx and nx <w and arr[ny][nx] == 1): #범위 안이면서 방문하지 않았다면
                queue.append((ny,nx))
                arr[ny][nx] = 0
    count += 1


while(1):
    w,h = map(int,input().split()) #너비, 높이
    if(w == 0 and h == 0):
        break
    arr = [list(map(int,input().split())) for _ in range(h)]

    count = 0
    for i in range(h):
        for j in range(w):
            if(arr[i][j]==1):
                bfs(i,j)

    print(count)
