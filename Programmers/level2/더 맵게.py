import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while (True):
        if (scoville[0] >= K):
            break
        else:
            if (len(scoville) > 1):
                heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
                answer += 1
            else:
                answer = -1
                break

    return answer