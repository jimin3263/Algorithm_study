#가장 인접한 두 공유기의 거리가 가능한 크게 설치
import sys
input = sys.stdin.readline

n, c = map(int, input().split()) #집 개수, 공유기 개수

#집 좌표 입력, 집은 수직선 위에 존재
arr = []
for _ in range(n):
    arr.append(int(input()))

#수직선 위에 있으므로 정렬부터
arr.sort()

#최소, 최대 길이 저장
start, end = 1, arr[-1] - arr[0]

result = []
while (start <= end):
    mid = (start+end) // 2 #중간 거리 값
    cur = arr[0] #현재 공유기 설치된 집
    cnt = 1 #공유기 설치 갯수
    tmp = float("inf")

    for i in arr:
        if(cur + mid <= i): #중간 거리 값과 현재 위치보다 크거나 같은 거리가 있다면 공유기 설치
            tmp = min(tmp, i-cur) #인접한 거리
            cnt += 1
            cur = i
    if (cnt < c): #설치한 공유기의 수가 목표한 수보다 작다면 왼쪽으로 옮긴다.
        end = mid - 1
    else:
        result.append(tmp)
        start = mid + 1

#print(result)
print(max(result))
