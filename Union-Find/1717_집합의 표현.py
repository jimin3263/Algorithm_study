import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

n, m = map(int, input().split()) #0-n까지 n+1개 집합

parent = [i for i in range(n+1)]

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(m):
    op, a, b = map(int, input().split())
    if op == 0: #합치기
        union(a, b)
    elif op == 1:
        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")
