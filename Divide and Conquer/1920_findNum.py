def find_num (s,e,k):
    if s>e:
        return 0
    m = (s+e)//2
    
    if arr1[m] == k:
        return 1
    #큰 경우
    elif arr1[m]<k:
        return find_num(m+1,e,k)
    #작은 경우
    else:
        return find_num(s,m-1,k)
  
        
n1 = int(input())
arr1=list(map(int,input().split()))
#오름차순 정렬
arr1.sort()
n2 = int(input())
arr2=list(map(int,input().split()))

for i in arr2:
    print(find_num(0,n1-1,i))






    
