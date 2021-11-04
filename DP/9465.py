#스티커
#바로 인접한 면은 계산 불가능
import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]

    for j in range(1,n): #1부터 시작
        if j == 1: # 두번째 스티커는 이전의 대각선만 더하기만 가능
            arr[0][j] += arr[1][j-1]
            arr[1][j] += arr[0][j-1]
        else:
            arr[0][j] += max(arr[1][j-1], arr[1][j-2])
            arr[1][j] += max(arr[0][j-1], arr[0][j-2])
            
    print(max(arr[0][n-1], arr[1][n-1]))
