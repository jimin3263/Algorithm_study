def dfs(v, visited):
    visited[v] = True
    w = arr[v]
    if not visited[w]:
        dfs(w, visited)
        
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.insert(0,0) #1부터 시작하도록 맞추기 위해서 인덱스0에 0을 넣음
    result = 0
    visited = [False] * (n+1)
    
    for i in range(1,n+1):
        if not visited[i]: #방문하지 않은 경우
            dfs(i, visited) #dfs 탐색
            result +=1
    print(result)
