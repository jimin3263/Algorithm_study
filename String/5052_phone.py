import sys
input = sys.stdin.readline

def find_num(arr):
    arr.sort()
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1][0:len(arr[i])]:
            return 'NO'
    return 'YES'

t=int(input())
ans = []
for i in range(t):
    n= int(input())
    arr = []
    for j in range(n):
        arr.append(input().strip())
    ans.append(find_num(arr))

print(*ans,sep='\n')
