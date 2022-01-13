import sys
n= int(input())
p= [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

zero=0 # 0
one=0 # 1
n_one=0 # -1
def divide(x,y,n):
    check = p[y][x]
    global zero,one,n_one

    for i in range(y,y+n):
        for j in range(x,x+n):
            # 가장 처음의 원소와 같지 않다면
            if p[i][j] != check:
                n=n//3
                for k in range(3):
                    for l in range(3):
                        # 9개로 분할
                        divide(x+n*l,y+n*k,n)
                return
                        
    if check == 0:
        zero+=1
        return
    elif check == 1:
        one+=1
        return
    elif check == -1:
        n_one+=1
        return

divide(0,0,n)
print(n_one)
print(zero)
print(one)

##############
# 결과값 딕셔너리로 저장 
# n = int(input())
# arr =[list(map(int,input().split())) for _ in range(n)]
# 
# result = {"-1": 0, "0": 0, "1": 0}
# def divide(y,x,n):
#     check = arr[y][x] #확인할 변수
#     for i in range(y, y+n): #처음부터 n만큼 탐색
#         for j in range(x, x+n):
#             if arr[i][j] != check: #탐색 중 일치하지 않는 것이 있다면
#                 n = n//3 #3으로 나눈다, 9개로 분리
#                 for k in range(3):
#                     for l in range(3):
#                         divide(y+n*k,x+n*l,n)
#                 return
# 
#     result[str(check)] += 1
# 
# 
# #-1, 0, 1
# divide(0,0,n)
# print(result["-1"])
# print(result["0"])
# print(result["1"])
