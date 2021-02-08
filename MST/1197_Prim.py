import sys
from heapq import heappush,heappop
V,E = map(int, sys.stdin.readline().split())
G=[[] for _ in range(V+1)]

for i in range(E):
    a,b,c = map(int, sys.stdin.readline().split())
    G[a].append((c,b))
    G[b].append((c,a))

def MST_prim():
    visited = [False]*(V+1)
    q=[(0,1)]
    result = 0
    while q:
        val,node=heappop(q)
        if not visited[node]:
            visited[node]=True
            result += val
            for val,ed in G[node]:
                if not visited[ed]:
                    heappush(q,(val,ed))
                    print(q)

    return result
print(MST_prim())
