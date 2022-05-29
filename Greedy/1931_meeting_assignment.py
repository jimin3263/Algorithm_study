import sys
n= int(input())
lec =[list(map(int,sys.stdin.readline().split())) for _ in range(n)]

#시작시간으로 정렬 후 종료시간으로 정렬
lec.sort(key=lambda x:x[0])
lec.sort(key=lambda x:x[1])

i=0
count=1
for j in range(1,n):
    #이전 회의의 종료시간 <= 이후 회의의 시작시간일 경우  
    if(lec[i][1]<=lec[j][0]):
        count+=1
        #이전 회의 <- 이후 회의 값 바꿔줌
        i=j
       
print(count)
