# Dynamic Programming
- 문제를 각각의 작은 문제로 나눠 해결한 결과를 저장해뒀다가 나중에 큰 문제의 결과와 합하여 풀이하는 알고리즘

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
