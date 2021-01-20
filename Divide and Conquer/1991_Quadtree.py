import sys
n= int(input())
p= [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]

def divide(x,y,n):
    check = p[y][x]
    check2= True
    # i == y축 , j == x축
    # n= 길이이므로 y부터 시작, y+n-1까지/ x부터 시작, x+n-1까지
    for i in range(y,y+n):
        for j in range(x,x+n):
            if p[i][j] != check:
                check2 = False
    if check2==True:
        print(check,end='')
    else:
        print("(",end='')
        divide(x,y,n//2) #2사분면
        divide(x+n//2,y,n//2)#1사분면
        divide(x,y+n//2,n//2)#3사분면
        divide(x+n//2,y+n//2,n//2)#4사분면
        print(")",end='')

divide(0,0,n)
