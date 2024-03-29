m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]

m = 6
n = 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
def solution(m, n, board):

    for i in range(m):
        board[i] = list(board[i])

    rm = set()
    answer = 0
    while True:
        for i in range(m-1):
            for j in range(n-1):
                current = board[i][j]
                if current == []:
                    continue
                if current == board[i+1][j] and current == board[i][j+1] and current == board[i+1][j+1]:
                    rm.add((i,j))
                    rm.add((i+1, j))
                    rm.add((i, j+1))
                    rm.add((i+1, j+1))

        if rm: #4x4 지웠다
            answer += len(rm)
            for i, j in rm:
                board[i][j] = []
            rm = set()
        else:
            return answer

        #새로 시작하기 전 빈칸 채우기
        while True:
            moved = 0
            for i in range(m-1):
                for j in range(n):
                    if board[i+1][j] == [] and board[i][j] != []:
                        board[i+1][j] = board[i][j]
                        board[i][j] = []
                        moved += 1
            if moved == 0:
                break


print(solution(m, n, board))