#2251
# A,B,C
# 처음- 앞의 두 물통 비어 있음, 세 번째 물통을 가득 차있음
# 어떤 물통에 들어있는 물을 다른 물통으로 쏟아 부을 수 있다.
# 한 물통이 비거나 다른 한 물통이 가득 찰 때까지 부을 수 있음 -> 둘 중에 작은 값을 구하도록 할 것
# 첫 번째 물통이 비어 있을 때, 세 번째 물통에 담겨있을 수 있는 물의 양을 모두 구해 내라

from collections import deque

a,b,c = map(int, input().split()) #각각의 부피, c는 가득 차 있다.
check = [[0] * 201 for i in range(201)] #1부터 200까지 가능
check[0][0] = 1
queue = deque()
queue.append([0,0])

answer = []

def pour(x,y): # x y의 현재 물통 양 확인
    if(not check[x][y]):
        check[x][y] = 1
        queue.append((x,y))

def bfs():
    while queue:
        x,y = queue.popleft()
        z = c-(x+y)
        if(x == 0): # a==0일 때 c의 물의 양
            answer.append(z)

        # a -> b
        # min(한 물통이 비는 경우, 다른 한 물통이 가득 찰 경우)
        water = min(x, b-y)
        pour(x-water, y+water)
        # a -> c
        water = min(x, c-z)
        pour(x-water, y)
        # b -> c
        water = min(y, c-z)
        pour(x, y-water)
        # b -> a
        water = min(y, a-x)
        pour(x+water, y-water)
        # c -> a
        water = min(z, a-x)
        pour(x+water, y)
        # c -> b
        water = min(z,b-y)
        pour(x,y+water)

bfs()
answer = sorted(answer)
print(" ".join(str(i) for i in answer))
