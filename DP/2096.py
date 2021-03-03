import sys
input = sys.stdin.readline
N = int(input())
min_arr = [[0]*3 for _ in range(2)]
max_arr = [[0]*3 for _ in range(2)]

arr = []
for i in range(N):
    arr=list(map(int, input().split()))
    max_arr[1][0] = arr[0] + max(max_arr[0][0],max_arr[0][1])
    min_arr[1][0] = arr[0] + min(min_arr[0][0],min_arr[0][1])

    max_arr[1][1] = arr[1] + max(max_arr[0][0], max_arr[0][1],max_arr[0][2])
    min_arr[1][1] = arr[1] + min(min_arr[0][0], min_arr[0][1],min_arr[0][2])

    max_arr[1][2] = arr[2] + max(max_arr[0][1], max_arr[0][2])
    min_arr[1][2] = arr[2] + min(min_arr[0][1], min_arr[0][2])

    for j in range(3):
        max_arr[0][j] = max_arr[1][j]
        min_arr[0][j] = min_arr[1][j]

print(max(max_arr[1]),min(min_arr[1]))
