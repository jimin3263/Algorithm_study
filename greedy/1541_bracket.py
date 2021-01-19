# - 직후 덧셈에 괄호치면 최솟값 구할 수 있음
# - 로 나눠서 리스트에 저장
# 55-50+40 의 경우 ['55','50+40']으로 저장
arr = input().split('-')
arr2=[]

# 덧셈 연산(괄호)
for i in arr:
    j_sum =0
    cnt=0
    s= i.split('+')
    for j in s:
        cnt+=1
        j_sum += int(j)
    if(cnt==len(s)):
        arr2.append(j_sum)

# 뺄셈
ans = arr2[0]
for i in range(1,len(arr2)):
    ans -= arr2[i]

print(ans)
