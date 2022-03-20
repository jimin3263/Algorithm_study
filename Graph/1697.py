#1697
#수빈이가 걷는다면 x-1, x+1
#순간이동 2*x
#수빈이가 동생을 찾는 가장 빠른 시간

n, k = map(int,input().split()) # 5, 17
visited = [0] * 100001

def bfs(n):
    queue = [n]
    while queue:
        x = queue.pop(0)
        if x == k:
            print(visited[k])
            break
        for i in (x-1, x+1, x*2): #4, 6, 10
            if 0 <= i <= 100000 and not visited[i]: #범위 안에 들어가고 방문한 적 없다면, not dist[i] -> 이미 채워졌다면 최소가 될 수 없음
                visited[i] = visited[x] + 1
                queue.append(i)

bfs(n)
