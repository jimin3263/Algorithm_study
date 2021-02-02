import sys
N,M = map(int,sys.stdin.readline().split())
arr=[list(map(int,sys.stdin.readline().strip())) for _ in range(N)]
x_list=[0,0,-1,1]
y_list=[-1,1,0,0]

#칸 수
count= [[False]*(M) for _ in range(N)]

#bfs
def maze(y,x):
    global count
    queue = [(y,x)]
    while queue:
        y,x = queue.pop(0)
        for i in range(4):
            go_y=y+y_list[i]
            go_x=x+x_list[i]
            if (0<=go_y<N and 0<=go_x<M):
                if count[go_y][go_x]==0 and arr[go_y][go_x]==1:
                    count[go_y][go_x]=count[y][x]+1
                    queue.append((go_y,go_x))

count[0][0]=1
maze(0,0)
print(count[N-1][M-1])
