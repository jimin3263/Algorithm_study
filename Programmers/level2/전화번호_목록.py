import heapq

def solution(phone_book):
    answer = True
    heapq.heapify(phone_book)
    
    while(phone_book):
        if(len(phone_book) == 1): #인덱스 범위 오류 
            return answer
        num = heapq.heappop(phone_book)
        if (num == phone_book[0][:len(num)]):
            answer = False
            return answer

    return answer
