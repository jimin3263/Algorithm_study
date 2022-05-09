import sys
input = sys.stdin.readline

def binarySearch(start, end):
    result = 0
    while(start <= end):
        mid = (start + end) // 2
        result_part = 0
        for i in arr:
            if mid < i:
                result_part += (i - mid)
        if (result_part == m):
            return mid
        elif (result_part < m) :
            end = mid - 1
        elif (result_part > m): #적어도m만큼의 떡, 조건 부합
            start = mid + 1
            result = mid

    return result


n,m = map(int, input().split())
arr = list(map(int, input().split()))
print(binarySearch(0, max(arr)))
