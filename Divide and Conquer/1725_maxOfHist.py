    
    
n = int(input())
arr=[]
result=0
for i in range(n):
    arr.append(int(input()))
arr.append(0)
stack = [(0,arr[0])]

for i in range(1,n+1):
    stack_num = i
    while(stack and arr[i]<stack[-1][1]):
        stack_num,temp = stack.pop()
        print(stack)
        result = max(result,temp*(i-stack_num))
    stack.append((stack_num,arr[i]))
    
print(result)  
