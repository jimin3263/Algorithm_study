import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]


def bfs():
    queue = deque()
    queue.append((0, 0))
    if visited[0][0] == 0:
        visited[0][0] = 1
    cnt = 0
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = dy[i] + y, dx[i] + x
            if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == 0: #방문하지 않았다면
                if arr[ny][nx] >= 1: #치즈 발견
                    arr[ny][nx] += 1
                elif arr[ny][nx] == 0: #빈 공간 발견
                    visited[ny][nx] = 1
                    queue.append((ny, nx))
                    cnt+= 1
    return cnt

time = 0
while True:
    visited = list([0] * m for _ in range(n))
    cnt = bfs()
    # for a in arr:
    #     print(a)
    # print()
    if n*m-1 == cnt:
        break
    for i in range(n):
        for j in range(m):
            if arr[i][j] >= 3:
                arr[i][j] = 0
            elif arr[i][j] > 0: #녹지 않은 부분은 다시 1로
                arr[i][j] = 1

    time += 1

print(time)