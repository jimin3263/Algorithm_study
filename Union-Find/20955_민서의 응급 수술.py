import sys
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        return find_parent(parent[x])
    return x

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split()) #뉴런, 시냅스
parent = [i for i in range(n+1)]
cnt = 0
for i in range(m):
    u, v = map(int, input().split())
    if find_parent(u) == find_parent(v):
        cnt += 1
    union_parent(u, v)

for i in range(1, n):
    if find_parent(i) != find_parent(i+1):
        union_parent(i, i+1)
        cnt += 1
print(cnt)