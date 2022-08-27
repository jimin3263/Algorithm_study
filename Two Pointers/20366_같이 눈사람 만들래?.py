import math
import sys
input = sys.stdin.readline

n = int(input())
snows = sorted(list(map(int, input().split())))

#1. 순서 필요없음 -> 정렬하자
# 0 1 2 3 4
# 2 3 5 5 9
min_diff = math.inf
for i in range(n):
    for j in range(i+3, n):
        snowman1 = snows[i]+snows[j]
        left, right = i+1, j-1
        while left <= right:
            snowman2 = snows[left] + snows[right]
            min_diff = min(min_diff, abs(snowman2- snowman1))

            if snowman2 > snowman1:
                right -= 1
            elif snowman2 < snowman1:
                left += 1
            else:
                min_diff = 0
                break
print(min_diff)

