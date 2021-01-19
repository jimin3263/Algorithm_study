import heapq  #우선순위 큐 자료구조 사용
import sys

n= int(input())
lec =[list(map(int,sys.stdin.readline().split())) for _ in range(n)]

#시작시간에 따라 정렬
#하나의 회의실에서 가능한 많이 회의할 수 있는 문제와 다름 (여러개의 강의실 가능)
lec.sort(key=lambda x:x[0])
lec_end=[0]

for i in range(n):
    #lec[i][0] = 시작시간
    # 종료 시간 <= 시작시간 경우가 있다면 저장해놨던 직전 종료 시간을 제거한 후, 새로운 종료 시간 업데이트
    if (lec_end[0]<=lec[i][0]):
        heapq.heappop(lec_end)
    heapq.heappush(lec_end,lec[i][1])

#종료시간의 갯수가 필요한 강의실의 갯
print(len(lec_end))
