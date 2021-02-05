import sys
N= int(sys.stdin.readline().strip())
M= int(sys.stdin.readline().strip())
city =[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
route= list(map(int,sys.stdin.readline().split()))

#1부터 시작하므로 1씩 빼줌
for i in range(M):
    route[i]-=1

visited=[False]*N
#첫번째 장소와 연결되어 있는 모든 경로 탐색
def dfs(v):
    global visited
    for i in range(N):
        if not visited[i] and city[v][i]==1:
            visited[i]=True
            dfs(i)


visited[route[0]]=True
dfs(route[0])

#여행 경로가 연결되어 있는 경로에 포함 되지 않으면 -> NO 출력
for i in range(1,M):
    if not visited[route[i]]:
        print("NO")
        break
    elif i==M-1:
        print("YES")
