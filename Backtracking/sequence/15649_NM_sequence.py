#중복없는 수열
#순서없음
N,M = map(int,input().split())
check = [False]*(N)
ans = [0]*M

def nm_sequence(a,n,m):
    if a == m:
        for i in range(m):
            print(ans[i],end =' ')
        print()
        return

    for i in range(n):
        #check[i]==True일때
        if check[i]:
            continue
        check[i]=True
        ans[a]=i+1
        nm_sequence(a+1,n,m)
        check[i]=False
    

nm_sequence(0,N,M)
############################

# import sys
# input = sys.stdin.readline

# n,m = map(int, input().split())

# #1~n 중에서 중복없이 m개 선택
# #증가하는 순으로 출력

# arr = [] #붙일 문자열 리스트
# def backtracking():
#     if (len(arr) == m):
#         print(" ".join(str(i) for i in arr))
#         return
#     for i in range(1,n+1):
#         if i not in arr:
#             arr.append(i)
#             backtracking()
#             arr.pop()

# backtracking()
