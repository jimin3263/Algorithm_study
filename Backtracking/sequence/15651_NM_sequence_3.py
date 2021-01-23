N,M = map(int,input().split())
check = [False]*N
ans = [0]*(M+1)

def nm_sequence(a,n,m):
    if(a == m ):
        for i in range(m):
            for j in range(i+1,m):
                if(ans[i]<=ans[j]):
                    print(ans[i],end=' ')
                    break
        print()
        return
    
    for i in range(n):
        ans[a]=i+1
        nm_sequence(a+1,n,m)

       
nm_sequence(0,N,M)
