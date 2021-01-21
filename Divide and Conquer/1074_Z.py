count = 0 
def draw_z (n,b,c):
    global count
    if n==2:
        for i in range(2):
            for j in range(2):
                count+=1
                if(i==b and j==c):
                    print(count-1)
                    return
    else:
        n = n//2
        count_mul= n**2
        #2사분면
        if(c<n and b<n):
            draw_z(n,b,c)
        #1사분면
        elif(c>=n and b<n):
            count+=count_mul
            draw_z(n,b,c%n)
        #3사분면
        elif(b>=n and c<n):
            count+=count_mul*2
            draw_z(n,b%n,c)
        #4사분면
        elif(b>=n and c>=n):
            count+=count_mul*3
            draw_z(n,b%n,c%n)
        return 

a,b,c = map(int,input().split())
a=2**a

draw_z(a,b,c)


