# 2칸 위로, 1칸 오른쪽 -2, +1
# 1칸 위로, 2칸 오른쪽 -1, +2
# 1칸 아래로, 2칸 오른쪽 +1, +2
# 2칸 아래로, 1칸 오른쪽 +2, +1
# 가장 왼쪽 아래 -> 병든 나이트가 여행에서 방문할 수 있는 칸의 최대 개수

n,m = map(int, input().split())

if n == 1:
    print(1)
elif n == 2:
    #이동횟수가 4보다 적지 않은 경우, 방법을 모두 사용해야한다.
    print(min(4,(m+1)//2))
else:
    if (m < 7):
        print(min(4,m))
    else:
        print(m-2)
