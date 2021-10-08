## 꼭 필요한 자료구조 기초

### 💡 탐색
- 많은 양의 데이터 중 원하는 데이터 찾는 과정 
- 대표적인 알고리즘: DFS, BFS

### 스택
- 배열 사용
- append(), pop()사용

### 큐
- from collections import deque 사용
- append(), popleft() 사용
- list(queue) 사용하면 리스트 자료형으로 반환

### 재귀 함수
- 종료 조건을 명시해줘야 함

```python
#반복
def factorial_iterative(n):
    result = 1
    
    for i in range(1, n+1):
        result *= i #1부터 n까지 곱함
        
    return result

#재귀
def factorial_recursive(n):
    if n <= 1: #n이 1보다 작을때 1 반환 
        return 1
    return n*factorial_iterative(n-1)
```

## DFS
- DFS: 깊이 우선 탐색 
- 스택, 재귀

```python
#DFS 예제

def dfs(graph, v, visited):
    #현재 노드 방문 처리
    visited[v] = True
    print(v, end=' ')

    #현재 노드와 연결된 다른 노드
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9
dfs(graph, 1, visited)
```

## BFS
- 너비 우선 탐색
- 큐
- BFS 구현이 더 빠르게 동작할 수 있음


```python
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    #큐가 빌때까지 반복
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]: #연결되어있는거 다 넣음  
            if not visited[i]:
                queue.append(i)
                visited[i] = True
```

## 문제 풀이

> 음료수 얼려 먹기  
> N x M 얼음 틀, 구멍 뚫린 부분 -> 0, 칸막이 1

```python
#음료수 얼려 먹기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr =[list(map(int,input().split())) for _ in range(n)]

def dfs(y, x):
    if x < 0 or x >= m or y < 0 or y >= n :
        return False
    if arr[y][x] == 0:
        arr[y][x] = 1 #방문 처리

        dfs(y, x-1) #좌
        dfs(y-1, x) #상
        dfs(y, x+1) #우
        dfs(y+1 ,x) #하

        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result +=1

print(result)
```
