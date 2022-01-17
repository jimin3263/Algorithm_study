#2447
#분할정복 
list = ["***", "* *", "***"]

def divide(n):
    if (n == 3):
        return list
    star = divide(n//3)
    new_star = []

    for i in star: 
        new_star.append(i*3)
    for i in star: #중간에 n//3 만큼의 공백 필요 
        new_star.append(i+" "*(n//3)+i)
    for i in star:
        new_star.append(i*3)

    return new_star

n = int(input()) #3의 거듭제곱
result = divide(n)

for i in result:
    print(i)
