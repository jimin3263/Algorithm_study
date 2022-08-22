import sys
r,c = map(int,sys.stdin.readline().split())
arr=[list(sys.stdin.readline().strip()) for _ in range(r)]
alphabet = [0] * 26

#상하좌우 이동
dy = [0,0,1,-1]
dx = [-1,1,0,0]

#같은 알파벳은 두 번 지날 수 없음
max_count = -1
def dfs(y,x, count):
    global max_count
    max_count = max(max_count, count)

    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0 <= ny < r and 0 <= nx < c and not alphabet[ord('Z')-ord(arr[ny][nx])]:
            alphabet[ord('Z')-ord(arr[ny][nx])] = 1
            dfs(ny, nx, count+1)
            alphabet[ord('Z')-ord(arr[ny][nx])] = 0

alphabet[ord('Z') - ord(arr[0][0])] = 1
dfs(0,0,1)
print(max_count)