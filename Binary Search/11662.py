#11662
#절대/상대 오차는 10-6
#삼분 탐색, 아래로 볼록인 함수일 때 사용
#거리 공식을 도함수로 나타내면 음에서 양으로 변하는 함수, 아래로 볼록일 것이다.. 
import sys
import math
input = sys.stdin.readline
ax, ay, bx, by, cx, cy, dx, dy = map(int, input().split())

lo, hi = 0, 100
result_dist = math.inf

def minho(p):
    #ax (출발점, 좌표를 구하므로 ax 더해준다) + bx-ax (거리) * 내분점 비율
    return (ax + (bx - ax) * (p / 100), ay + (by - ay) * (p / 100))

def gangho(p):
    return (cx + (dx - cx) * (p / 100), cy + (dy - cy) * (p / 100))

while (abs(hi-lo) > 1e-7): #오차 설정
    #1:2 내분
    internal1 = (2*lo+hi)/3
    #2:1 내분
    internal2 = (lo+2*hi)/3
    #민호
    minho_internal1 = minho(internal1) #1:2 에서의 좌표값
    minho_internal2 = minho(internal2) #2:1 에서의 좌표값
    #강호
    gangho_internal1 = gangho(internal1)
    gangho_internal2 = gangho(internal2)
    #1:2 내분 점에서 민호 강호의 거리
    dist1 = math.sqrt((minho_internal1[0]- gangho_internal1[0]) ** 2 + (minho_internal1[1]- gangho_internal1[1]) ** 2)
    #2:1 내분 점에서 민호 강호의 거리
    dist2 = math.sqrt((minho_internal2[0]- gangho_internal2[0]) ** 2 + (minho_internal2[1]- gangho_internal2[1]) ** 2)
    result_dist = min(result_dist, min(dist1, dist2))
    #print(result_dist)
    if (dist1 > dist2): #시작점 ~ dist1구간에는 최솟값 존재하지 않음
        lo = internal1
    else:
        hi = internal2

print('%.10f' %result_dist)
