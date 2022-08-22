import sys
r,c = map(int,sys.stdin.readline().split())
arr=[list(sys.stdin.readline().strip()) for _ in range(r)]

#상하좌우 이동
dy = [0,0,1,-1]
dx = [-1,1,0,0]

result = 0
def bfs(y,x):
    global result
    q = set()
    q.add((y,x,arr[y][x]))
    while q:
        y,x,step = q.pop()
        result = max(result, len(step))
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < r and 0 <= nx < c and arr[ny][nx] not in step:
                q.add((ny, nx, step+arr[ny][nx]))

bfs(0,0)
print(result)