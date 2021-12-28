#11725
#트리 -> 그래프로 나타냄, 1부터 탐색하도록  
import sys
sys.setrecursionlimit(10 ** 5)
n = int(input()) #노드 개수

tree = [[] for _ in range(n + 1)]
parents = [0 for _ in range(n + 1)] #부모노드 저장 

#트리 -> 그래프로 생성
for _ in range(n-1):
    i, j = map(int, input().split())
    tree[i].append(j)
    tree[j].append(i)

#print(tree)
def dfs(v):
    for i in tree[v]:
        if parents[i] == 0: #부모 노드 설정이 되어있지않다면
            parents[i] = v
            dfs(i)


dfs(1) #트리의 루트는 1 즉 1부터 탐색
print("\n".join(str(parents[i]) for i in range(2, n+1)))
#print(parents)
