#중복없이 M개를 고른 수열
N,M = map(int,input().split())
check = [False]*N
ans = [0]*M

def nm_sequence(a,b,n,m):
    if(a == m ):
        for i in range(m):
            print(ans[i],end=' ')
        print()
        return
    
    for i in range(b,n):
        if check[i]:
            continue
        check[i]=True
        ans[a]=i+1
        nm_sequence(a+1,i+1,n,m)
        check[i]=False
       
nm_sequence(0,0,N,M)
