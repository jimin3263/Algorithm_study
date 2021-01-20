import sys
A, B, C = map(int,sys.stdin.readline().split())

def divide_mul(a,b):
    if b==1:
        return a
    #b가 홀수일 때
    elif b%2 ==1:
        d=divide_mul(a,b-1)
        return d*a%C
    #b가 짝수
    else:
        d=divide_mul(a,b//2)
        d%=C
        return d**2%C
    
print(divide_mul(A,B)%C)
