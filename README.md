# Algorithm_study

## References
- 파이썬 알고리즘 인터뷰  
- BOJ  
- SW Expert Academy

## Week Study
|날짜|문제유형|
|------|---|
|1.7~1.14|[Greedy](https://github.com/jimin3263/Algorithm_study/tree/main/greedy)|
|1.15~1.21|[Divide and Conquer](https://github.com/jimin3263/Algorithm_study/tree/main/Divide%20and%20Conquer)|
|1.22~1.28|[Back Tracking](https://github.com/jimin3263/Algorithm_study/tree/main/Backtracking)|
|1.29~2.4|[Graph](https://github.com/jimin3263/Algorithm_study/tree/main/Graph)|
|2.5~2.11|[MST](https://github.com/jimin3263/Algorithm_study/tree/main/MST)|
|2.19~2.25|[String](https://github.com/jimin3263/Algorithm_study/tree/main/String)|
|2.26~3.4|[DP](https://github.com/jimin3263/Algorithm_study/tree/main/)|


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
