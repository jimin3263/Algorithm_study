#2331

a, p = map(int,input().split())

num = [a]
while(True):
    a = str(a) 
    sum = 0
    for i in range(len(a)):
        sum += int(a[i]) ** p
    if sum in num:
        break
    num.append(sum)
    a = sum

print(num.index(sum))

# 숫자로 푸는 법
# while a: 
#   sum += ((a%10) ** p) 
#   a //= 10
