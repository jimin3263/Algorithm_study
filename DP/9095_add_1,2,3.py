import sys
input = sys.stdin.readline

T = int(input())
# 1=1 -> 1개
# 2=2 / 1+1 ->2개
# 3= 1+2/ 2+1 /1+1+1/3 ->4개
arr =[1,2,4]
# n<11 이므로 배열에서 9까지 저장
for i in range(3,10):
    arr.append(arr[i-1]+arr[i-2]+arr[i-3])
for i in range(T):
    n = int(input())
    print(arr[n-1])
    
'''
4 = 1+3 (3으로 만들 수 있는 수 -> 4)
  = 2+2 (2 -> 2)
  = 3+1 (1 -> 1)
'''
