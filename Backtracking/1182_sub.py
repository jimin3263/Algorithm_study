#부분집합, 중복선택안됨, 순서존재

N,S = map(int,input().split())
arr = list(map(int,input().split()))

check=[False]*N
result=[]
count =0

def sequence(N,S,arr,check,d):
    global count
    global result
    #길이가 0 이거나 합이 S와 같으면
    if len(result) and sum(result)== S:
        count+=1
        
    for i in range(d,N):
        if check[i]:
            continue
        check[i] = True
        result.append(arr[i])
        sequence(N,S,arr,check,i+1)
        result.pop()
        check[i]=False


sequence(N,S,arr,check,0)
print(count)
