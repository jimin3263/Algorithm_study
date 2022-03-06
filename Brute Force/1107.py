#1107
#시작 채널 = 100
import sys
input=sys.stdin.readline

n = int(input()) #이동하고자 하는 채널
m = int(input()) #고장난 버튼 개수
broken_button = list(input().split()) #고장난 버튼 목록

#100부터 시작, n까지의 최솟값
result = abs(100-n) #한 칸씩 이동한다면 가능한 횟수

def possible_button(n):
    n = list(str(n))
    for i in n:
        if i in broken_button:
            return False
    return True

# 0 ≤ N ≤ 500,000/ - 하는 경우도 존재 하므로 1000000
for i in range(1000001):
    if (possible_button(i) is True):
        result = min(result, len(str(i)) + abs(n-i))

print(result)
