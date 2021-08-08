# Dynamic Programming
- 문제를 각각의 작은 문제로 나눠 해결한 결과를 저장해뒀다가 나중에 큰 문제의 결과와 합하여 풀이하는 알고리즘
- **큰 문제를 작은 문제로** 나눌 수 있거나 **작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일**할 때 사용

|알고리즘|풀이 가능한 문제들의 특징|풀이 가능한 문제 및 알고리즘|
|------|---| --- |
|DP|최적 부분 구조, 중복된 하위 문제들|0-1 배낭 문제, 피보나치 수열|
|Dreedy|최적 부분 구조, 탐욕 선택 속성|분할 가능 배낭 문제|
|Divide-and-conquer|최적 부분 구조|병합 정렬, 퀵정렬|

**1. Bottom-Up (Tabulation)**  
- 더 작은 하위 문제부터 살펴본 다음, 작은 문제의 정답을 이용해 큰 문제의 정답을 풀어나감  
- 일반적으로 이 방식을 DP라고 칭함
```python
#fibo_bottom-up
def fib(n):
    dp[0]=0
    dp[1]=1 
    for i in range(2,n+1):
        dp[i]= dp[i-1]+dp[i-2]
    return dp[n]
```
```python
#0-1_knapsack_bottom-up
cargo = [
    #(price,weight)
    (4,12),
    (2,1),
    (10,4),
    (1,1),
    (2,2)
]

def knapsack(cargo):
    capacity = 15
    pack =[]
    for i in range(len(cargo)+1):
        pack.append([])
        for c in range(capacity+1):
            #0번째 행,열은 0으로 세팅
            if i==0 or c==0:
                pack[i].append(0)
            #현재 물건 가격 + (c-현재 물건 무게)일 때의 최대 가격
            #현재 물건 추가 안했을때의 최대 가격
            elif cargo[i-1][1] <= c:
                pack[i].append(max(cargo[i-1][0]+pack[i-1][c-cargo[i-1][1]],pack[i-1][c]))
            else:
                pack[i].append(pack[i-1][c])
    return pack[-1][-1]
```

**2. Top-Down (Memorization)**
- 하위 문제에 대한 정답을 계산했는지 확인해가며 문제를 풀어나감
```python
#fibo_top-down
def fib(n):
    if n<=1:
        return n    
    if dp[n]:
        return dp[n]
    dp[n]=fib(n-1)+fib(n-2)
    return dp[n]
```

### 1로 만들기
> 1. 5로 나누어떨어지면 5로 나눔
> 2. 3으로 나누어떨어지면 3으로 나눔
> 3. 2로 나누어떨어지면 2로 나눔  
> 4. x에서 1을 뺌

```python
import sys
input = sys.stdin.readline

x = int(input())
arr = [5,3,2]
dp = [0] * (x+1)#bottom-up

for i in range(2,x+1):
    dp[i]=dp[i-1]+1

    for j in arr:
        if(i%j == 0):
            dp[i] = min(dp[i//j]+1, dp[i])

print(dp[x])
```

### 개미 전사
> 인접한 창고는 털 수 없음  
> 최대한 많은 식량을 얻는 방법  

```python
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

dp = [0]* n

dp[0] = arr[0]
dp[1] = max(arr[1],arr[0])

#i번째를 털건지 체크할 때 i-1 까지의 최적해, i-2까지의 최적해 + i번째 식량을 고려하면 됨
for i in range(2,n):
    dp[i] = max(arr[i]+dp[i-2], dp[i-1])

print(dp[n-1])
```

### 바닥 공사
> 가로 N x 세로 2   
> 1x2, 2x1, 2x2 덮개로 채우는 모든 경우의 수  

```python
#i-1까지 채워져 있으면 2X1
#i-2까지 채워져 있으면 1X2 두개 or 2X2
import sys
input = sys.stdin.readline

n = int(input())
dp = [0]* (n+1)

dp[1]=1
dp[2]=3
for i in range(3,n+1):
    dp[i] = dp[i-1] + dp[i-2]*2

print(dp[n])
```

### 효율적인 화폐 구성
> N가지 종류의 화폐 존재, 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합을 M원이 되도록 함  

```python
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
list = []
for i in range(n):
    list.append(int(input()))

dp = [10001] * (m+1)
dp[0] = 0

for i in list:
    for j in range(i, m+1):
        if (dp[j - i] != 10001): #화폐로 만들 수 있다면
            dp[j] = min(dp[j-i]+1 ,dp[j])

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])
```

### 11066
<img src= "https://user-images.githubusercontent.com/50178026/111514330-faf1eb00-8794-11eb-9583-f597abf407df.png" width="50%" height="50%"/>
<img src= "https://user-images.githubusercontent.com/50178026/111514990-9f742d00-8795-11eb-93b5-a8da476b4a75.jpg" width="50%" height="50%"/>

