#9466
import sys
sys.setrecursionlimit(10 ** 5) #2 ≤ n ≤ 100,000
t = int(input())

#사이클 확인은 dfs를 이용해 search하면서 list에 저장하고, 방문했던 w가 나오면 cycle에 w가 있는지 확인한다.
def dfs(v, visited):
    global result
    cycle.append(v) #사이클 확인 4,7,6
    visited[v] = True
    w = student[v]
    if not visited[w]:
        dfs(w, visited)
    else:
        if w in cycle:#4
            result += cycle[cycle.index(w):] #사이클 시작부터 끝까지 result 배열에 추가한다.

for _ in range(t):
    n = int(input())
    visited = [False] * (n+1)
    student = [0] + list(map(int,input().split()))
    result = []  #팀이 가능한 사람 목록 저장
    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            dfs(i, visited)
    print(n-len(result))
