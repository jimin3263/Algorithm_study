n =int(input())
arr = list(map(int,input().split()))
arr2=[0]*n

for i in range(n):
    for j in range(n):
        if(arr[i]==0 and arr2[j]==0):
            arr2[j]=i+1
            break;
        elif(arr2[j]==0):
            arr[i]-=1

for i in range(n):
    print(arr2[i],end=' ')
        
