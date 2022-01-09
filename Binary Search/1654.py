#1654
import sys
input = sys.stdin.readline

k, n = map(int, input().split()) #가지고 있는 랜선 수 -> 같은 길이의 n개의 랜선 수
arr = []

for i in range(k):
    arr.append(int(input()))

start, end = 1, max(arr)
result = 0 #결과 저장
while (start <= end):
    mid = (start+end) // 2 #분할할 랜선의 길이
    line = 0 #라인 갯수

    for x in arr:
        line += x//mid #분할한 랜선 수
    if line < n: #n개의 랜선보다 더 적게 잘랐다면, mid를 왼쪽으로 옮겨야 함
        end = mid - 1
    else:
        result = mid #최대한 덜 잘라야하므로 여기에
        start = mid+1

print(result)
