#10819
#차이를 최대로
import itertools
n = int(input())
arr = list(map(int, input().split()))

result = 0
ans = 0
def sub_add(list):
    global ans
    result = 0
    for i in range(1,n):
        result += abs(list[i]-list[i-1])
    ans = max(ans, result)

for i in itertools.permutations(arr,n): #순열
    sub_add(i)
print(ans)
