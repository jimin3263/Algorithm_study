#10971
#1~n 도시 존재, 외판원이 한 도시에서 출발 -> n개의 도시 모두 거침
#w[i][j]는 i -> j로 가는 비용, i->j 갈 수 없는 경우는 0
n = int(input())
w =[list(map(int,input().split())) for _ in range(n)]

result_min = float("inf")

def dfs(start, now, value, visited): 
    global result_min
    if len(visited) == n and w[now][start] != 0: #모두 방문, 다시 처음으로 돌아간다면
        result_min = min(result_min, value + w[now][start])

    for i in range(n):
        if(i not in visited and w[now][i] != 0): #방문하지 않았고 방문하고자 하는 곳이 방문할 수 있다면 이동
            visited.append(i)
            dfs(start, i, value+w[now][i], visited)
            visited.pop()

for i in range(n):
    visited = [i]
    dfs(i,i,0,visited)#시작 지점, 현재 지점, 총 이동 value, 방문 기록
print(result_min)
