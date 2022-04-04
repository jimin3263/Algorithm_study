from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)

    while progresses:
        while progresses[0] < 100:
            for i in range(len(progresses)):
                progresses[i] += speeds[i]

        #첫 번째가 100이 넘는다면 다음 것들 중에서 100 넘는거 있는지 확인
        cnt = 0
        while progresses:
            if (progresses[0] >= 100):
                cnt += 1
                progresses.popleft()
                speeds.popleft()
            else:
                break
        answer.append(cnt)
    return answer
