#1707
#22:49
#각 노드에서 탐색하면서 연결된 부분은 반대 그룹으로 속함
#반대 그룹으로 나누면서 이미 방문한 노드에서 같은 그룹이 존재한다면 -> False
#배열이 아닌 연결리스트로 구현 -> 배열시 메모리 초과
import sys
input = sys.stdin.readline

k = int(input())

def bfs(node):
    queue = [node]
    visited[node] = 1
    while queue:
        node = queue.pop(0)
        for i in adj[node]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[node] * (-1) #연결된 노드는 반대 색을 채워줌
            elif visited[i] == visited[node]: #방문 했으며, 같은 색이라면
                return False
    return True

for i in range(k):
    v, e = map(int,input().split())
    adj = [[] for _ in range(v+1)]
    for j in range(e):
        x, y = map(int, input().split())
        adj[x].append(y)
        adj[y].append(x)
    visited = [0] * (v+1)
    ans = True
    for j in range(1,v+1):
        if visited[j]==0 and not bfs(j): #여러 그래프로 나뉘어지는 경우도 있음
            ans = False
            break
    print("YES" if ans else "NO")
