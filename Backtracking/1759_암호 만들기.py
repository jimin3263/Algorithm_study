import copy
import sys
input = sys.stdin.readline

l, c = map(int, input().split()) #서로 다른 c개, 증가하는 순서, l개의 갯수
arr = list(input().split())
arr = sorted(arr) #암호는 증가하는 순서
vowels = ['a', 'e', 'i', 'o', 'u']

#라이브러리쓰지 않고 구현
string_temp = []
result = []
visited = []
def combination(array, length, index):
    if len(string_temp) == length:
        result.append(copy.deepcopy(string_temp))
        return

    #각 원소를 한 번만 뽑도록
    for i in range(index, len(array)):
        if i in visited:
            continue
        string_temp.append(array[i])
        visited.append(array[i])
        combination(array, length, i + 1)
        string_temp.pop()
        visited.pop()

combination(arr, l, 0)

for password in result:
    # 최소 한개의 모음, 최소 두개의 자음

    #모음 갯수 센다
    cnt = 0
    for p in password:
        if p in vowels:
            cnt += 1

    if cnt >= 1 and l-cnt >= 2:
        print("".join(password))