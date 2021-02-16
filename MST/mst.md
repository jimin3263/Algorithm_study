# MST
## MST의 특징  
Minimum Spanning Tree : spanning tree 중에서 사용된 간선들의 가중치 합이 최소인 트리
1. n개 노드, (n-1)개의 간선
2. Acyclic graph
3. connected
4. 간선의 가중치 합이 최소

## 구현 방법
### Kruskal Algorithm
- 간선 선택 기반
1. 간선들을 가중치의 오름차순으로 정렬
2. 사이클을 형성하지 않으면서 가장 낮은 가중치를 선택함
3. 해당 간선을 MST 집합에 추가 되어 있지 않다면 집합에 추가함 (union, find 이용)
```python
root = [_ for _ in range(n)]
def find(x):
  if x == root[x]:
    return x
  else:
    return find(root[x])

def union(a, b):
  root_a, root_b = find(a), find(b)
  root[root_b] = root_a
 
# 가중치의 오름차순으로 정렬
dist.sort(key=lambda x:x[2])

# 연결해 나감
while dist:
  cur = dist.pop(0)
  # 연결 되어 있지 않다면
  if find(cur[0]) != find(cur[1]):
    # 연결
    union(cur[0],cur[1])

```

### Prim Algorithm
- 노드 선택 기반
1. 앞 단계에서 만들어진 MST 집합에 인접한 노드 중에서 최소 간선으로 연결된 정점을 선택해서 트리 확장
2. (N-1)개의 간선을 가질 때까지 반복
```python
# 방문 확인 리스트
visited = [False]*(V+1)
# 처음 방문(weight=0, node=1)
q=[(0,1)]
while q:
  w,node=heappop(q)
  if not visited[node]:
    visited[node]=True
    for val,ed in G[node]:
      if not visited[ed]:
        heappush(q,(val,ed))
```


