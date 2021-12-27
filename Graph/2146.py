#2146
#한 섬과 한 섬을 잇는 다리 중 가장 짧은 길이
import sys
input = sys.stdin.readline
from collections import deque

dx = [0,0,-1,1] #상하좌우
dy = [1,-1,0,0]

#입력받는 부분
n = int(input())
arr =[list(map(int,input().split())) for _ in range(n)]

#섬 구별 필요, 숫자를 바꾸자 -> bfs
queue = deque()
def bfs(y,x):
    queue.append((y,x))
    arr[y][x] = count #기준이 되는 부분 누락되지 않도록 while문 이전에 숫자 변경
    while (queue):
        y,x = queue.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if( 0<= ny and ny< n and 0 <= nx and nx < n and arr[ny][nx] == 1):
                arr[ny][nx] = count
                queue.append((ny,nx))

count = 2 #섬 구별을 위한 숫자
for i in range(n):
    for j in range(n):
        if (arr[i][j] == 1):  # 섬부분 나오면 탐색 시작
            bfs(i, j)
            count+=1

# print(arr)

# #연결 확인 -> 최소거리: bfs
def bfs_connection(island):
    global ans
    dist = list([-1] * n for _ in range(n)) #거리를 위한 배열
    queue = deque()

    for i in range(n):
        for j in range(n):
            if arr[i][j] == island: #현재 탐색하고자 하는 섬
                queue.append((i,j))
                dist[i][j] = 0 #출발점이므로 0
                
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            #1. 범위 벗어나는 경우
            if( 0 > ny or ny >= n or 0 > nx or nx >= n):
                continue
            #2. 이동한 곳이 바다라면
            if(arr[ny][nx] == 0 and dist[ny][nx] == -1):
                dist[ny][nx] = dist[y][x] + 1
                queue.append((ny,nx))
            #3. 이동한 곳이 본인의 섬이 아닌 새로운 섬인 경우 -> 본인 섬 아니고 바다도 아니어야 함
            if(arr[ny][nx] != island and arr[ny][nx] != 0):
                ans = min(ans, dist[y][x]) #이동 전 거리와 원래 담았던 거리 중 더 작은 값
                return


ans = sys.maxsize
for i in range(2, count):
    bfs_connection(i)
print(ans)
