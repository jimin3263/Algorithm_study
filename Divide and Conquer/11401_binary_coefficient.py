p = 1000000007
#입력 값이 커서 런타임 에러 -> 페르마 소정리 이용
'''
#1 파스칼 법칙
count=0
def binary(a,b):
    global count
    if b==0 or a==b:
        count+=1
    else:
        binary(a-1,b-1)
        binary(a-1,b)

    return count
'''
#2 페르마 소정리
# a*a^p-2≡1 (mod p) -> a^p-2은 a의 역원

#a^b
def divide_mul(a,b):
    if b==1:
        return a
    #b가 홀수
    elif b%2 ==1:
        d=divide_mul(a,b-1)
        return d*a%p
    #b가 짝수
    else:
        d=divide_mul(a,b//2)
        d%=p
        return d**2%p

#n!
def fac(n):
    result=1
    for i in range(1,n+1):
        result *=i
        result%=p
    return result

n,k = map(int,input().split())
k=min(k,n-k)

#분모
b = fac(k)*fac(n-k)
b=divide_mul(b,(p-2))%p

#분자
a = fac(n)

print((a*b)%p)

