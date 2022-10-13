import sys

input = sys.stdin.readline

t = int(input())  # 테스트 케이스 개수
for i in range(t):
    n, m, k = map(int, input().split())  # 집의 개수, 돈을 훔칠 연속된 집의 개수, 최소 돈의 양
    arr = list(map(int, input().split()))  # n개의 집에서 각각 보관중인 돈의 양

    left, right = 0, m - 1
    curr_sum = sum(arr[left:right + 1])
    answer = 0

    if n == m:
        if curr_sum < k:
            answer += 1
    else:
        while right < n + m - 1 and left <= right:
            if curr_sum < k:  # 가능
                answer += 1
            right += 1
            curr_sum -= arr[left % n]
            curr_sum += arr[right % n]
            left += 1

    print(answer)
