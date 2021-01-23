N,M = map(int,input().split())
check = [False]*(N)
ans = [0]*M

def nm_sequence(a,n,m):
    if a == m:
        for i in range(m):
            print(ans[i],end =' ')
        print()
        return

    for i in range(n):
        #check[i]==True일때
        if check[i]:
            continue
        check[i]=True
        ans[a]=i+1
        nm_sequence(a+1,n,m)
        check[i]=False
    

nm_sequence(0,N,M)
            
