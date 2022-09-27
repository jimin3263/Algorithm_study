import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n = int(input()) #전체 사람의 수
a, b = map(int, input().split())
m = int(input()) #관계의 개수

graph = defaultdict(list)
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def bfs():
    visited = [0] * (n + 1)
    visited[a] = 1
    queue = [(a, 0)]
    queue = deque(queue)
    while queue:
        curr, cnt = queue.popleft()
        if curr == b:
            return cnt
        for i in graph[curr]:
            if not visited[i]:
                visited[i] = True
                queue.append((i, cnt+1))
    return -1

#bfs로 찾음
print(bfs())


