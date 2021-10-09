from itertools import permutations
def check(num):
    if (num < 2):
        return False
    for i in range(2,num):
        if num % i == 0:
            return False #소수 아님
    return True #소수


def solution(numbers):
    answer = []
    num = [_ for _ in (numbers)] # 한 글자씩 분리

    for i in range(1, (len(numbers)+1)):
        l = list(map(''.join, permutations(num, i))) #순열 -> list

        for j in l:
            if check(int(j)):
                answer.append(int(j))

    return len(set(answer)) #중복 제거 위해서 set씀
