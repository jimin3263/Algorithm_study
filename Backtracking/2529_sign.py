k = int(input())
arr = list(input().split())

#방문했던 노드인지 확인
check=[False]*10
min=""
max=""

#부등호 조건 확인
def check2(b,i,j):
    if b ==">":
        return i>j
    return j>i

def back (k,c,arr,s):
    global min,max
    if (k+1)==c:
        #가장 처음 만들어지는 문자열 -> 최소
        if not len(min):
            min=s
        #마지막 문자열 -> 최대
        else:
            max=s
        return

    for i in range(10):
        if not check[i]:
            if c==0 or check2(arr[c-1],s[-1],str(i)):
                check[i]=True
                back(k,c+1,arr,s+str(i))
                check[i]=False

back(k,0,arr,"")
print(max)
print(min)
