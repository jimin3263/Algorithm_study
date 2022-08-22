import sys
input = sys.stdin.readline

n = int(input())
board = [0] * n #보드
result = 0
def check(x): #위, 오른쪽 대각선, 왼쪽 대각선에 있는지 확인
    for i in range(x):
        if board[i] == board[x]:
            return False #못두는 경우
        elif abs(board[x] - board[i]) == x - i:
            return False
    return True

def queen(x):
    global result
    if x == n: #행이 끝난다면
        result += 1
    else:
        for i in range(n): #열 맞추는 중
            board[x] = i  # x행 i열에 둔다
            if check(x):
                queen(x+1)

queen(0)
print(result)