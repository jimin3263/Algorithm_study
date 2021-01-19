n= int(input())
time = list(map(int,input().split()))

time.sort()
min_sum=0
i_sum=0

for i in range(n):
    min_sum += (i_sum+time[i])
    i_sum = i_sum+time[i]

print(min_sum)
