#시작 2:04
#n: 정점, m: 간선

#dfs 
n,m=map(int,input().split())

#인접 표시할 이차원 배열
adj = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    x,y = map(int,input().split())
    adj[x][y],adj[y][x]=1,1

visited_dfs = [False] * (n+1)
def dfs(v):
    visited_dfs[v] = True
    for i in range(1,n+1):
        if not visited_dfs[i] and adj[v][i] == 1:
            dfs(i)

cnt = 0
for i in range(1, n+1):
    if not visited_dfs[i]:
        dfs(i)
        cnt+=1

print(cnt)

#bfs
'''
#n: 정점, m: 간선
n,m=map(int,input().split())

#인접 표시할 이차원 배열
adj = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    x,y = map(int,input().split())
    adj[x][y],adj[y][x]=1,1

visited_bfs = [False] * (n+1)
def bfs(v):
    visited_bfs[v] = True
    queue = [v]
    while queue:
        v= queue.pop(0)
        for i in range(1,n+1):
            if not visited_bfs[i] and adj[v][i] == 1:
                queue.append(i)
                visited_bfs[i] = True

cnt = 0
for i in range(1, n+1):
    if not visited_bfs[i]:
        bfs(i)
        cnt+=1

print(cnt)
'''
