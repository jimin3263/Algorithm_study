import sys
a,b = map(int,sys.stdin.readline().split())
arr = []
arr=[list(sys.stdin.readline().strip()) for _ in range(a)]

#사용한 알파벳인지 확인
#사용하지 않음:False, 사용함:True
alpha = [False]*26
max_count=0

def back(x,y,count):
    global max_count,alpha
    
    #상,하,좌,우 이동
    x_list =[0,0,1,-1]
    y_list =[-1,1,0,0]
    
    max_count=max(max_count,count)
    
    for i in range(4):
        go_x=x+x_list[i]
        go_y=y+y_list[i]
        #index를 벗어날 수 있으므로 조건 걸어줌
        if(0 <= go_x <a and 0<=go_y<b):
            #아스키코드로 변환
            check = ord(arr[go_x][go_y]) - 65
            if alpha[check]:
                continue
            alpha[check]=True
            back(go_x,go_y,count+1)
            alpha[check]=False
            
alpha[ord(arr[0][0])-65]=True
back(0,0,1)
print(max_count)

    
