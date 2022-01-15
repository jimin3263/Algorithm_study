#11729
#한 번에 한 개의 원판
#위의 것이 아래의 것보다 작아야 한다.

n = int(input())

result = []
#n = 남은 갯수, fr = 이동 전, to = 이동 후, other = 나머지
#n-1를 1 -> 2
#마지막 것을 1 -> 3
#n-1을 2 -> 3
def hanoi(n, fr, other, to): #가장 처음: 1,2,3 (1 -> 3으로 옮겨야 한다.)
    if (n <= 0): #다 옮긴 경우
        return
    #1에 있는 것을 2로 옮긴다.
    hanoi(n-1, fr, to, other)
    result.append((fr,to))
    #2에 있는 것을 3으로 옮긴다.
    hanoi(n-1, other, fr, to)

hanoi(n, 1, 2, 3)
print(len(result))
for fr, to in result:
    print(fr, to)
