import sys
from heapq import heappush,heappop
V,E = map(int, sys.stdin.readline().split())
G=[[] for _ in range(V+1)]

for i in range(E):
    a,b,c = map(int, sys.stdin.readline().split())
    G[a].append((b,c))
    G[b].append((a,c))

def MST_prim():
    visited = [False]*(V+1)
    q=[(1,0)]
    result = 0
    while q:
        node,val=heappop(q)
        if not visited[node]:
            visited[node]=True
            result += val
            for ed,val in G[node]:
                if not visited[ed]:
                    heappush(q,(ed,val))

    return result
print(MST_prim())
