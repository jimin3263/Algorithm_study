M = int(input())
N = int(input())
arr = list([0]*(M+1) for _ in range(M+1))

#방문 확인
visited=[False]*(M+1)

for i in range(N):
    a,b = map(int,input().split())
    arr[a][b],arr[b][a]=1,1

count =0

#BFS
def virus(v):
    global count,visited
    queue = []
    queue.append(v)
    while queue:
        v=queue.pop()
        for i in range(1,M+1):
            if not visited[i] and arr[v][i]==1:
                count+=1
                visited[i]=True
                queue.append(i)

visited[1]=True
virus(1)
print(count)
