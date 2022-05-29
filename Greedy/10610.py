#10610
#30의 배수는 3의 배수이면서 일의 자리가 0인 수, 3의 배수는 각 자리 숫자의 합이 3의 배수인 수
n = input()
n = sorted(n,reverse=True)

def multiple_30():
    sum = 0
    if '0' not in n:
        return -1
    for i in n:
        sum += int(i)
    if sum % 3 != 0:
        return -1
    else:
        return ''.join(n)

print(multiple_30())
