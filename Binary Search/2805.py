# (1 ≤ N ≤ 1,000,000, 1 ≤ M ≤ 2,000,000,000) -> 조건에서 일단 binary search
import sys
input = sys.stdin.readline
n, m = map(int,input().split()) #나무 수, 상근이가 가지고 가는 나무 길이
arr = list(map(int,input().split()))

start, end = 0, max(arr)
while (start <= end):
    mid = (start+end) // 2
    result = 0
    for i in arr:
        if (i > mid): #자르고자 하는 기리보다 길다면
            result += i - mid #자르고 남은 길이 저장

    if(result < m): #실제로 잘라야하는 길이보다 짧다면, 더 자름 (왼쪽으로 옮김)
        end = mid - 1
    else:
        ans = mid  #높이의 최댓값 저장이므로 오른쪽으로 옮기는 곳에서 ans 저장  
        start = mid + 1

print(ans)
