import sys
import copy
N,M = map(int,sys.stdin.readline().split())
arr=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
max_count =0
#벽세움
def wall(n,arr):
    global max_count
    if n==3:
        count=virus()
        max_count= max(max_count,count)

    else:
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 0:
                    arr[i][j] = 1
                    wall(n+1,arr)
                    arr[i][j]=0


x_list = [0,0,-1,1]
y_list = [-1,1,0,0]

def virus():
    queue = []
    num_2=[]
    # arr를 arr2에 복사함
    # deepcopy를 하지 않으면 arr도 바뀜
    arr2 = copy.deepcopy(arr)
    # 2인 위치 저장
    for i in range(N):
        for j in range(M):
            if(arr2[i][j]==2):
                num_2.append((i,j))
    # 2 주변 탐색         
    while num_2:
        queue.append(num_2.pop(0))
        while queue:
            y,x=queue.pop(0)
            for k in range(4):
                go_x = x_list[k] + x
                go_y = y_list[k] + y
                if (0<=go_x<M and 0<=go_y<N and arr2[go_y][go_x]==0):
                    arr2[go_y][go_x]=2
                    queue.append((go_y,go_x))
    # 0 갯수 셈
    count=0
    for i in range(N):
        count = count+arr2[i].count(0)
    return count

wall(0,arr)
print(max_count)
