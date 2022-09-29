import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]

# 벽 1개 깰 수 있음 DP? 2개 사용?
dp1 = list([0] * m for _ in range(n))  # 깨지 않음
dp2 = list([0] * m for _ in range(n))  # 깬 경우

visited = list([0] * m for _ in range(n))
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

def bfs():
    queue = deque()
    queue.append((0, 0, 0))
    dp1[0][0] = 1
    visited[0][0] = 1
    while queue:
        y, x, flag = queue.popleft()
        if y == n-1 and x == m-1:
            return dp2[-1][-1] if flag == 1 else dp1[-1][-1]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m: #구간 확인
                if arr[ny][nx] == 1 and flag == 0: #벽이라 깬다면
                    dp2[ny][nx] = dp1[y][x] + 1
                    queue.append((ny, nx, 1))
                    visited[ny][nx] = 1
                elif arr[ny][nx] == 0 and flag == 1: #벽을 이미 깼다면
                    if not dp2[ny][nx]:
                        dp2[ny][nx] += dp2[y][x] + 1
                        queue.append((ny, nx, flag))
                elif arr[ny][nx] == 0 and flag == 0: #벽을 하나도 안깬 상태
                    if not dp1[ny][nx]:
                        dp1[ny][nx] += dp1[y][x] + 1
                        queue.append((ny, nx, flag))
    return -1

result = bfs()

if result == -1:
    print(-1)
else:
    print(result)