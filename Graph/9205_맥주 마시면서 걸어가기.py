import math
import sys
from collections import deque

input = sys.stdin.readline

t = int(input())  # 테스트 케이스
for _ in range(t):
    n = int(input())  # 편의점 개수
    sy, sx = map(int, input().split())  # 상근이네 집
    c_list = []  # 편의점 좌표
    for i in range(n):
        y, x = map(int, input().split())
        c_list.append((y, x))
    ry, rx = map(int, input().split())  # 락페

    queue = deque([(sy, sx)])
    visited = [0] * (n+1)

    def bfs(queue):
        while queue:
            curr_y, curr_x = queue.popleft()
            if abs(curr_y - ry) + abs(curr_x - rx) <= 1000:
                print("happy")
                return
            for i in range(n):
                if not visited[i]:
                    cy, cx = c_list[i]
                    if abs(cy-curr_y) + abs(cx-curr_x) <=1000:
                        visited[i] = 1
                        queue.append((cy, cx))

        print("sad")

    bfs(queue)
