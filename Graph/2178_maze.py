# import sys
# N,M = map(int,sys.stdin.readline().split())
# arr=[list(map(int,sys.stdin.readline().strip())) for _ in range(N)]
# x_list=[0,0,-1,1]
# y_list=[-1,1,0,0]

# #칸 수
# count= [[False]*(M) for _ in range(N)]

# #bfs
# def maze(y,x):
#     global count
#     queue = [(y,x)]
#     while queue:
#         y,x = queue.pop(0)
#         for i in range(4):
#             go_y=y+y_list[i]
#             go_x=x+x_list[i]
#             if (0<=go_y<N and 0<=go_x<M):
#                 if count[go_y][go_x]==0 and arr[go_y][go_x]==1:
#                     count[go_y][go_x]=count[y][x]+1
#                     queue.append((go_y,go_x))

# count[0][0]=1
# maze(0,0)
# print(count[N-1][M-1])

#2178, 새로 푼 버전 
# 1. count와 같이 새로운 공간을 추가하지 않도록 해도 된다. -> 다녀온 길은 횟수로 업데이트하므로 count 배열을 통해 방문 확인 필요 없다.
# 2. deque의 popleft() 시간복잡도: O(1) / 리스트의 pop() 시간복잡도: O(n)

#미로, 이동할 최소의 칸 -> bfs
import sys
from collections import deque
input = sys.stdin.readline

dx = [0,0,-1,1] #상하좌우
dy = [1,-1,0,0]

n,m = map(int, input().split()) #세로, 가로
arr = [list(map(int,input().strip())) for _ in range(n)]

def bfs(y,x):
    queue = deque()
    queue.append((y,x)) #0,0 에서 출발하도록 할거임

    while (queue):
        y,x = queue.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if (0 <= ny and ny < n and 0 <= nx and nx < m and arr[ny][nx] == 1): #이동할 수 있는 경우
                arr[ny][nx] = arr[y][x] + 1
                queue.append((ny,nx))


bfs(0,0)
print(arr[n-1][m-1])
