#중복가능 수열
#순서없음
N,M = map(int,input().split())
ans = [0]*M

def nm_sequence(a,n,m):
    if(a == m ):
        for i in range(m):
            print(ans[i],end=' ')
        print()
        return
    
    for i in range(n):
        ans[a]=i+1
        nm_sequence(a+1,n,m)

       
nm_sequence(0,N,M)
