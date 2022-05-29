# Greedy Algorithm
- 당장 좋은 것만 선택하는 그리디
- 현재 선택이 나중에 미칠 영향에 대해서는 고려하지 않음
- '가장 큰 순서대로', '가장 작은 순서대로'와 같은 기준을 제시해줌 -> 정렬 알고리즘

## 거스름돈
> 거스름돈으로 500, 100, 50, 10원짜리 동전이 무한히 존재  
> 거슬러 줘야 할 돈이 N원일 때, 거슬러 줘야 할 동전의 최소 개수  


```python
# 내 풀이
import sys
input = sys.stdin.readline

Change = [500, 100, 50, 10]

def min_change(n):
    cnt = 0
    for i in Change:
        cnt+=n//i
        n%=i
    print(cnt)

n = int(input())
min_change(n)
```

*-> 동전의 단위가 배수 형태여서 그리디로 풀이 가능*

## 큰 수의 법칙
> 배열의 크기: N (2<= N <= 1000)  
> M번 더해서 가장 큰 수 만드는 법칙  
> 단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없음

```python
# 내 풀이
import sys
input = sys.stdin.readline

#N: 배열 크기, M: 최대 더할 수 있는 횟수, K: 최대 연속 허용
N,M,K = map(int,input().split())
arr = list(map(int,input().split()))

#내림차순 정렬
arr.sort(reverse=True)

#가장 큰 숫자, 두 번째로 큰 숫자만 반복해서 사용하면 됨
first = arr[0]
second = arr[1]

#first K번 더하고 second 1번 더하기
sum = 0
for i in range(M):
    if(K % (i+1) == 0):
        sum += second
    else:
        sum += first

print(sum)
```

```python
#저자 풀이
import sys
input = sys.stdin.readline

#N: 배열 크기, M: 최대 더할 수 있는 횟수, K: 최대 연속 허용
N,M,K = map(int,input().split())
arr = list(map(int,input().split()))

#내림차순 정렬
arr.sort(reverse=True)

#가장 큰 숫자, 두 번째로 큰 숫자만 반복해서 사용하면 됨
first = arr[0]
second = arr[1]

# 한 세트: K + 1
# 큰 수의 갯수: M//(K+1) 횟수 반복, * K 
# 나누어 떨어지지 않을 때: M % (K+1)
count = (M // (K + 1)) * K
count += M % (K + 1)

result = 0
result = count * first
result += (M - count) * second

print(result)
```

## 숫자 카드 게임
> 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장 뽑음  
> N X M 형태, 각 행에서 가장 작은 숫자 뽑음  
> 마지막으로 뽑는 카드가 가장 커야 함

```python
# 내 풀이
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
min_arr =[]

# 각 행에서 최솟값 선택
for i in range(N):
    arr = list(map(int, input().split()))
    min_arr.append(min(arr))

# 고른 것 중에서 최댓값 선택
print(max(min_arr))
```

```python
result = 0
for i in range(n):
        data = list(map(int, input().split()))
        min_value = min(data)
        # 배열에 저장하지 않고 max 값 변수에 저장함
        result = max(result, min_value)

```

## 1이 될 때까지
> N이 1이 될 때까지 두 과정 중 하나 반복  
> 1. N에서 1을 뺀다.
> 2. N을 K로 나눈다.

```python
# 내 풀이
import sys
input = sys.stdin.readline

N, K = map(int,input().split())

#N에서 K로 나누어지면 나눔, 나눌 수 없으면 1

cnt = 0
while (N!=1):
    if(N % K == 0):
        N //=K
    else:
        N-=1

    cnt += 1

print(cnt)
```

```python
# 저자 풀이
n, k = map(int, input().split())

result = 0
while True:
    # K로 나누어 떨어지는 수가 될 때까지 1을 뺌(한 번에)
    target = (n // k) * k
    result += n - target  
    n = target
    # N이 K보다 작을 때 반복문 탈출
    if n < k:
        break
    result += 1
    n //= k  
    
# 1이 될 때까지 이므로 
result += (n - 1)

print(result)
```
