#7576
#하루 뒤 익지 않은 토마토는 근처 익은 토마토에 의해서 익게 된다. -> bfs

import sys
from collections import deque
input = sys.stdin.readline

dx = [0,0,-1,1] #상하좌우
dy = [1,-1,0,0]

m, n = map(int, input().split()) #가로, 세로
arr =[list(map(int,input().split())) for _ in range(n)]

#1: 익음, 0: 익지 않음, -1: 토마토 존재하지 않음
def bfs():
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if (0 <= nx and nx <m and 0<=ny and ny < n and arr[ny][nx] == 0):
                arr[ny][nx] = arr[y][x] + 1 #날짜 증가
                queue.append((ny,nx))


queue = deque() #첫 날 익은 토마토 queue에 일단 저장
for i in range(n):
    for j in range(m):
        if (arr[i][j] == 1): #익은 토마토라면 주변 탐색 -> 익도록 하고 하루 지나도록 한다.
            queue.append((i,j))

bfs()

def count_day():
    max_day = -1
    for i in range(n):
        for j in range(m):
            if(arr[i][j] == 0): #익지 못한 토마토가 존재한다면
                return -1

        max_day = max(max_day, max(arr[i]))

    return max_day -1 #1부터 시작했으므로 빼줘야한다..

print(count_day()) 
