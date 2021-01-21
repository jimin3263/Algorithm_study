def hist(l,r):
    #가로 == 1
    global h
    if (l==r):
        return h[l]
    m = (l+r)//2
    #가로가 1 일때 최댓값
    result = max(hist(l,m),hist(m+1,r))
    #가로가 2일 때 최댓값 
    div_l = m
    div_r = m+1
    height = min(h[div_l],h[div_r])
    result = max(result,height*2)

    #확장
    while(l< div_l or div_r<r):
        #오른쪽으로 확장
        #왼쪽은 확장할 수 있는 만큼 다함: div_r<r and div_l == l
        #최댓값을 구하기 위해더 높은 쪽 부터 확장:div_r<r and h[div-l-1]<h[div_r+1]
        if(div_r<r and ((div_l==l) or h[div_l-1] < h[div_r+1])):
            div_r+=1
            height = min(height,h[div_r])
        
        else:
            div_l-=1
            height = min(height,h[div_l])
        result = max(result, height*(div_r - div_l+1))

    return result
    
    
    

n = int(input())
h=[]
for i in range(n):
    h.append(int(input()))

print(hist(0,n-1))
