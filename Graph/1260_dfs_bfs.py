N,M,V= map(int,input().split())

#인접 표시할 이차원 배열
adj = [[0]*(N+1) for _ in range(N+1)]

for i in range(M):
    x,y = map(int,input().split())
    adj[x][y],adj[y][x]=1,1
#방문 여부
visited = [False]*(N+1)

def dfs(visited,v):
    visited[v]= True
    print(v, end=' ')
    for i in range(1,N+1):
        if not visited[i] and adj[v][i] == 1:
            dfs(visited,i)

def bfs(v):
    visited_bfs = [False] * (N + 1)
    visited_bfs[v] = True
    queue = [v]
    while queue:
        v= queue.pop(0)
        print(v,end=' ')
        for i in range(1,N+1):
            if not visited_bfs[i] and adj[v][i] == 1:
                queue.append(i)
                visited_bfs[i]=True

dfs(visited,V)
print()
bfs(V)
