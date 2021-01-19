n= int(input())
time = list(map(int,input().split()))

#오름차순으로 정렬
time.sort()


# 1 == 1
# 1+2 == 3
# 1+2+3 == 6

# 1+3+6 == 최종 구하는 최소 시간

'''
min_sum=0 #전체 시간의 합
i_sum=0 # 1+2+3 의 경우, 1+2까지의 값

for i in range(n):
    min_sum += (i_sum+time[i])
    i_sum = i_sum+time[i]
'''
min_sum=0 #전체 시간의 합
for i in range(n):
    min_sum += time[i]*(n-i)
    


print(min_sum)
