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
