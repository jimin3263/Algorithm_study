#9663
#n*n에서 n개의 퀸을 둔다고 할 때 공격할 수 없는 횟수
#가로, 세로, 대각선 불가능

n = int(input())
arr = [-1] * n #배열 index == row, 배열 값 == col

cnt = 0
def back(row):
    global cnt
    if (row == n): #가로 끝까지 놔뒀다면
        cnt += 1
        return

    for i in range(n):
        flag = True
        arr[row] = i
        for j in range(row): #이전 row의 위치 확인
            #세로, 대각선 위치 확인
            #대각선이면 .. (1,2)  -> (2,3) or (2,1) // (3,0) or (3,4)
            if arr[j] == arr[row] or abs(j - row) == abs(arr[j] - arr[row]):
                flag = False
                break
        if (flag):
            back(row+1)

back(0)
print(cnt)
