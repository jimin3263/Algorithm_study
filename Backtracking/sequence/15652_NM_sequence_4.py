#중복가능 수열
#오름차순
N,M = map(int,input().split())
ans = [0]*M

def nm_sequence(a,b,n,m):
    if(a == m):
        for i in range(m):
            print(ans[i],end=' ')
        print()
        return
    
    for i in range(b,n):
        ans[a]=i+1
        nm_sequence(a+1,i,n,m)

       
nm_sequence(0,0,N,M)
