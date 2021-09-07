# Binary Search
- 탐색 범위를 반으로 줄여나가면서 데이터를 빠르게 탐색하는 탐색 기법  
- 내부의 데이터가 정렬되어 있을 때만 사용
- **시작점**, **끝점**, **중간점** 변수 사용

> 반복문으로 구현  
```python
def binary_search(array, target, start, end):
    while start <= end :
        mid= (start+end)//2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1 #중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        else:
            start = mid + 1 #중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    return None

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)

if result == None:
    print("원소 존재하지 않음")
else:
    print(result+1)
```

### 부품 찾기
> N개의 부품 중에서 M개의 부품이 존재하는지 확인  

```python
import sys
input = sys.stdin.readline

def binary_search(array, target, start, end):
    while start <= end :
        mid= (start+end)//2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


#존재하는 부품
n = int(input())
array = list(map(int, input().split()))
array.sort()

#손님 요청
m = int(input())
array2 = list(map(int, input().split()))

for i in array2:
    result = binary_search(array, i, 0, n-1)
    if result == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')
```

### 떡볶이 떡 만들기

> 절단기의 길이보다 크다면 잘릴 것이며 손님이 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값은?  

```python
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int, input().split()))
start, end = 0, max(arr)

result = 0 #결과 담음
while(start <= end):
    total = 0
    mid = (start+end) // 2
    for x in arr:
        if x > mid: #떡이 더 길다면 잘라야 함
            total += x-mid #자르고 남은 떡의 길이
    if total < m: #떡이 모자란 경우 -> 더 많은 떡을 잘라야 하므로 end 조정
        end = mid - 1
    else: #떡이 남는 경우 -> 덜 잘라도 되므로 start 조정
        result = mid
        start = mid + 1


print(result)
```
