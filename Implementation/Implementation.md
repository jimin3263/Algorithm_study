## Implementation
- 머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정
- 완전 탐색, 시뮬레이션
- 이동 관련해서 dy, dx 배열 사용, ny, nx 이용해서 체크, 조건 확인 후 y,x 값 결정  


### 예제 - 상하좌우
> (1,1) 에서 출발, 공간 밖을 벗어나면 무시

```python
import sys
input = sys.stdin.readline
n = int(input())
arr = list(input().split())

# L,R,U,D
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

move_types = ['L','R','U','D']

x,y = 1,1 #출발 지점
for plan in arr:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    #공간을 벗어나는 경우
    if nx < 1 or ny <1 or nx > n or ny > n :
        continue #무시
    x, y = nx, ny #공간 벗어나지 않으면 이동

print(y, x)
```

### 예제 - 시각
> 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중, 3이 하나라도 포함되는 모든 경우의 수 -> 완전 탐색 이용

```python
import sys
input = sys.stdin.readline
n = int(input())

count = 0
for i in range(n+1): #시
    for j in range(60): #분
        for k in range(60): #초
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)
```

### 실전 - 왕실의 나이트
> 수평으로 두 칸 이동한 뒤, 수직으로 한 칸 이동  
> 수직으로 두 칸 이동한 뒤, 수평으로 한 칸 이동  
> 모든 경우의 수 계산, 제약 조건 확인

```python
import sys
input = sys.stdin.readline
input_data = input()

row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1 #(1,1)을 시작점으로 둠

#수평 두 칸 이동(좌, 우), 수직 한 칸 이동(상, 하) -> 4가지
#수직 두 칸 이동, 수평 한 칸 이동 -> 4가지
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, -2), (-1, -2), (1, 2), (1, -2)]

result = 0

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if 1 <= next_row  and next_row <= 8 and 1 <= next_column and next_column <= 8:
        result += 1

print(result)
```

### 실전 - 게임 개발
> 왼쪽 방향부터 차례대로 갈 곳 정함, 가보지 않은 칸 존재하면 왼쪽 방향 회전 후 왼쪽으로 한 칸 전진/ 가보지 않은 칸이 없다면 회전만 함  
> 네 방향 모두 이미 가본 칸 or 바다 -> 바라보는 방향 유지, 1단계로 돌아감, 바다인 경우 움직임 멈춤

```python
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
y, x, dir = map(int,input().split())

#방문한 위치 저장
d = [[0] * m for _ in range(n)]
d[y][x] = 1

#전체 맵 입력
arr=[]
for i in range(n):
    arr.append(list(map(int, input().split())))

#북,동,남,서
dy=[-1,0,1,0]
dx=[0,1,0,-1]

#현재 위치에서 왼쪽 방향부터 회전 -> -1
def turn_left():
    global dir
    dir-=1
    if dir == -1:
        dir = 3

cnt = 1
turn_time = 0 #회전 횟수 저장, 4일 때 -> 뒤로 가거나 바다면 멈추거나
while True:
    turn_left()
    nx = x + dx[dir]
    ny = y + dy[dir]

    if d[ny][nx] == 0 and arr[ny][nx] == 0: #가보지 않음, 육지
        d[ny][nx] = 1
        y, x = ny, nx
        cnt +=1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        #뒤로
        ny = y - dy[dir]
        nx = x - dx[dir]
        if arr[ny][nx] == 0 :
            y,x = ny, nx
            turn_time = 0
        else:
            break

print(cnt)
```
