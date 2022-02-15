#1744
#두 수 묶어서 곱한 뒤 최대 합 구하기
#모든 수는 묶거나 묶지 않아야 한다.

n = int(input())
positive_arr = [] #9,8,7 ~~
negative_arr = [] #-9,-8,-7, ~~ -> 0 포함해야함

positive_result = 0
negative_result = 0

#음수 양수 분리
for i in range(n):
    k = int(input())
    if(k == 1): #1은 곱하면 수가 더 작아지므로 먼저 더하도록 한다.
        positive_result += 1
    elif(k > 0):
        positive_arr.append(k)
    else:
        negative_arr.append(k)

positive_arr = sorted(positive_arr, reverse=True)
negative_arr = sorted(negative_arr)

positive_len = len(positive_arr)
negative_len = len(negative_arr)

def addNum(length, arr, add_result):
    if (length % 2 == 0):  # 짝수라면 두 개씩 묶음
        for i in range(0, length, 2):
            add_result += arr[i] * arr[i + 1]
    else: #홀수라면 두 개씩 계산 후 마지막 더함
        for i in range(0, length - 1, 2):
            add_result += arr[i] * arr[i + 1]
        add_result += arr[length - 1]
    return add_result


positive_result = addNum(positive_len, positive_arr, positive_result)
negative_result = addNum(negative_len, negative_arr, negative_result)

print(positive_result + negative_result)
