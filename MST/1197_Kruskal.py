import sys
V,E = map(int, sys.stdin.readline().split())
p =[i for i in range(V+1)]
rank = [0 for i in range(V+1)]

G=[]
for i in range(E):
    a,b,c = map(int, sys.stdin.readline().split())
    G.append([a,b,c])

G.sort(key=lambda x:x[2])

def find(x):
    if p[x]==x:
        return x
    else:
        y=find(p[x])
        p[x]=y
        return y

def union(x,y):
    x= find(x)
    y= find(y)
    if x!=y:
        if rank[x] > rank[y]:
            p[y]=x
        else:
            p[x]=y
            if rank[x]==rank[y]:
                rank[y]+=1

count =0
count_v=0
for i in range(E):
    v = G[i][0]
    u = G[i][1]
    w = G[i][2]
    if find(v) != find(u):
        union(v,u)
        count+=w
        count_v+=1
    if count_v == V-1:
        break
print(count)
