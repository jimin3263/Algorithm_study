import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]


visited = list([0] * n for _ in range(n))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(y, x, type):
    queue = deque()
    queue.append((y, x))
    visited[y][x] = 1
    curr = arr[y][x]
    target = []
    if type == 1 and (curr == "R" or curr == "G"):
        target.extend(["R", "G"])
    else:
        target.append(curr)

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and arr[ny][nx] in target:
                visited[ny][nx] = 1
                queue.append((ny, nx))

answer = []
for k in range(2):
    visited = list([0] * n for _ in range(n))
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j, k)
                cnt += 1
    answer.append(cnt)

print(*answer)