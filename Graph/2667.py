#2667
import sys
input = sys.stdin.readline

dx = [0,0,-1,1] #상하좌우
dy = [1,-1,0,0]

n = int(input())

arr = [list(map(int,input().strip())) for _ in range(n)]
count_list=[]

#bfs
def bfs(y,x,count): #queue 이용
    queue = [(y,x)]
    arr[y][x] = 0 #방문 표시

    while(queue):
        y,x = queue.pop()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if(0<=ny and ny< n and 0<=nx and nx <n and arr[ny][nx] == 1):
                queue.append((ny,nx))
                count += 1
                arr[ny][nx] = 0

    count_list.append(count)


for i in range(n):
    for j in range(n):
        count = 1
        if(arr[i][j]==1):
            bfs(i,j,count)

count_list.sort() #오름차순 정렬
print(len(count_list))
print("\n".join(str(i) for i in count_list))

