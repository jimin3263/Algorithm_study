# k개 연속 -> 할인
import sys
import heapq
from collections import Counter

input = sys.stdin.readline
n, d, k, c = map(int, input().split())  # 접시 수, 초밥의 가짓수, 연속해서 먹는 접시의 수, 쿠폰 번호
arr = []
for i in range(n):
    arr.append(int(input()))

i, j = 0, k
counter = Counter(arr[:k])
counter[c] += 1

max_select = []
heapq.heappush(max_select, (-1) * len(counter))

while True:
    if j == n + k - 1:
        break
    counter[arr[i]] -= 1
    if counter[arr[i]] == 0:
        del counter[arr[i]]
    counter[arr[j % n]] += 1

    len_counter = len(counter)
    heapq.heappush(max_select, (-1) * len_counter)
    i += 1
    j += 1

print(heapq.heappop(max_select) * (-1))
