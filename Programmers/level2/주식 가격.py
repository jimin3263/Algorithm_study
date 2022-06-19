from collections import deque

def solution(prices):
    prices = deque(prices)
    answer = []
    while(prices):
        price = prices.popleft()
        cnt = 0
        for p in prices:
            cnt += 1
            if price > p:
                break
        answer.append(cnt)
    return answer