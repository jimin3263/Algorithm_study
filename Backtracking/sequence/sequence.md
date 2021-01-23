N:1부터 N까지 자연수에서
M:길이가 M인 수열

1. 중복없음, 순서없음
[15649](https://www.acmicpc.net/problem/15649)
2. 중복없음, 순서존재(오름차순)
[15650](https://www.acmicpc.net/problem/15650)
3. 중복가능, 순서없음
[15651](https://www.acmicpc.net/problem/15651)
4. 중복가능, 순서존재(오름차순)
[15652](https://www.acmicpc.net/problem/15652)
---------------
1. 중복없음
+ check 리스트 사용

```python
#숫자 N만큼 배열 할당
check=[False]*N 

for i in range(n):
        if check[i]:
            continue
         #check 리스트가 True일때는 아래과정 무시
         #사용한 숫자에 True로 표시
        check[i]=True
        ans[a]=i+1
        nm_sequence(a+1,n,m)
        check[i]=False #자식노드를 다 탐색한 후, 이 과정을 통해 check가 모두 False로 됨
```

2. 순서존재
+ 매개변수 추가


```python
#매개변수 b 추가
def nm_sequence(a,b,n,m):
    …
    #for문에서 i의 시작점을 하나씩 증가시켜 수열을 오름차순으로 배열할 수 있음.
    for i in range(b,n):
        if check[i]:
            continue
        check[i]=True
        ans[a]=i+1
        nm_sequence(a+1,i+1,n,m)
        check[i]=False

``` 
