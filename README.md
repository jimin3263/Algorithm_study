# Algorithm

## References
- 파이썬 알고리즘 인터뷰  
- BOJ  
- SW Expert Academy

## Contents
|문제유형|
|---|
|[Greedy](https://github.com/jimin3263/Algorithm_study/tree/main/greedy)|
|[Divide and Conquer](https://github.com/jimin3263/Algorithm_study/tree/main/Divide%20and%20Conquer)|
|[Back Tracking](https://github.com/jimin3263/Algorithm_study/tree/main/Backtracking)|
|[Graph](https://github.com/jimin3263/Algorithm_study/tree/main/Graph)|
|[MST](https://github.com/jimin3263/Algorithm_study/tree/main/MST)|
|[String](https://github.com/jimin3263/Algorithm_study/tree/main/String)|
|[DP](https://github.com/jimin3263/Algorithm_study/tree/main/DP)|


## Timeout
> C++
```c++
ios_base :: sync_with_stdio(false); 
cin.tie(NULL);
cout.tie(NULL);
```

> Python
```python
import sys
input = sys.stdin.readline
# 맨 끝 개행문자 포함하므로 input().rstrip()사용
```

## Input
> 공백있는 정수 입력
```python
#1 2
N,M = map(int,input().split())
```
> 1차원 배열 입력
```python
#2 1 1 0
arr = list(map(int,input().split()))
```
> 공백있는 2차원 배열 입력
```python
'''
1 4
3 5
0 6
5 7
3 8
'''
arr =[list(map(int,input().split())) for _ in range(n)]
```
> 공백없는 2차원 배열 입력
```python
'''
1111
1111
0001
'''
arr = [list(map(int,input().strip())) for _ in range(n)]
```

## Runtime Error
```python
# 최대 재귀 깊이 변경
import sys
sys.setrecursionlimit(10 ** 6)
```
