import sys

n= int(sys.stdin.readline())
star=[tuple(map(float,sys.stdin.readline().split())) for i in range(n)]
dist=[]

#거리 계산
for i in range(n):
  for j in range(i+1,n):
    star_a = star[i]
    star_b = star[j]
    distance = round(((star_a[0]-star_b[0])**2 + (star_a[1]-star_b[1])**2)**0.5,2)
    dist.append([i,j,distance])

#정렬
dist.sort(key=lambda x:x[2])

root = [_ for _ in range(n)]

# 크루스칼 알고리즘
def find(x):
  if x == root[x]:
    return x
  else:
    return find(root[x])

def union(a, b):
  root_a, root_b = find(a), find(b)
  root[root_b] = root_a

ans= 0
while dist:
  cur = dist.pop(0)
  # 연결 되어 있지 않다면
  if find(cur[0]) != find(cur[1]):
    ans += cur[2]
    # 연결
    union(cur[0],cur[1])
print(ans)
