### 그래프 표현
> 딕셔너리를 이용해 인접리스트로 구현
```python
graph ={
    1:[2,3,4],
    2:[5],
    3:[5],
    4:[],
    5:[6,7],
    6:[],
    7:[3]
}
```

#### 1. DFS
> 재귀 이용
```python
def recursive_dfs(v,visited=[]):
    visited.append(v)
    for w in graph[v]:
        if w not in visited:
           recursive_dfs(w,visited)
    return visited # 방문한 결과 반환
```
> 스택 이용
```python
def iterative_dfs(v):
    visited=[]
    stack = [v]
    while stack:
        v=stack.pop()
        if v not in visited:
            visited.append(v)
            for w in graph[v]:
                stack.append(w)
    return visited
```

#### 2. BFS
> 큐 이용
```python
def iterative_bfs(v):
    visited=[v]
    queue =[v]
    while queue:
        v=queue.pop(0)
        for w in graph[v]:
            if w not in visited:
                visited.append(w)
                queue.append(w)
    return visited
```
