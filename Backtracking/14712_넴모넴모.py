import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0] * m for _ in range(n)]

def dfs(count):
    global answer

    if count == n*m:
        answer += 1
        return

    y, x = count//m, count % m
    #아무것도 놔두지 않는 경우
    dfs(count+1)

    #놔두는 경우
    if graph[y-1][x-1] == 0 or graph[y-1][x] == 0 or graph[y][x-1] == 0:
        graph[y][x] = 1
        dfs(count+1)
        graph[y][x] = 0

answer = 0
dfs(0)
print(answer)