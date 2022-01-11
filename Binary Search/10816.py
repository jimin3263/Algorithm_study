n = int(input()) #숫자 카드 개수
arr1 = list(map(int,input().split())) #숫자 카드에 적힌 정수
m = int(input())
arr2 = list(map(int,input().split())) #가지고 있는 카드인지 확인하기 위함

arr1.sort() #정렬된 배열에서 이진탐색 가능

dic = dict() #개수 파악을 위한 딕셔너리 생성

for i in arr1:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

def binary_search(arr1, start, end, target):
    while (start <= end):
        mid = (start + end) // 2
        if (arr1[mid] == target):
            return mid
        elif (arr1[mid] < target):
            start = mid + 1
        else:
            end = mid - 1
    return None

for i in arr2:
    if (binary_search(arr1, 0, n-1, i) == None):
        print("0", end=' ')
    else:
        print(dic[i], end=' ')
