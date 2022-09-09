import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
max_value = max(map(max, arr))

visited = list([0] * n for _ in range(n))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(y, x, k):
    queue = deque()
    queue.append((y, x))
    visited[y][x] = 1
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and arr[ny][nx] > k:
                visited[ny][nx] = 1
                queue.append((ny, nx))

answer = 0
for k in range(max_value):

    visited = list([0] * n for _ in range(n))

    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > k and not visited[i][j]:
                bfs(i, j, k)
                cnt += 1

    answer = max(answer, cnt)

print(answer)

