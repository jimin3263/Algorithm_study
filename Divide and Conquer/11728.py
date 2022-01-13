#11728
#분할 정복
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
#정렬되어있는 배열 입력
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

combine = [] #합쳐질 인덱스

i, j = 0, 0 #n,m 인덱스
while (i<n) and (j<m):
    if arr1[i] < arr2[j]:
        combine.append(arr1[i])
        i += 1
    else:
        combine.append(arr2[j])
        j += 1

if (i == n): #i가 끝까지 갔다면
    combine += arr2[j:]
else:
    combine += arr1[i:]

print(' '.join(map(str,combine)))
