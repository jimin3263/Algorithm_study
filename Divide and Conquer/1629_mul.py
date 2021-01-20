import sys
A, B, C = map(int,sys.stdin.readline().split())

def divide_mul(a,b):
    if b==1:
        return a
    elif b%2 ==1:
        return divide_mul(a,b-1)*a%C
    else:
        d=divide_mul(a,b//2)
        d%=C
        return d**2%C
    
print(divide_mul(A,B)%C)
