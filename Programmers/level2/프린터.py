from collections import deque

def solution(priorities, location):
    priorities = deque(priorities)
    pri_idx = deque(list(i for i in range(len(priorities))))
    result_dic = dict()
    order_idx = 1
    while (len(priorities) != 0):
        if (priorities[0] == max(priorities)):
            priorities.popleft()
            result_dic[pri_idx.popleft()] = order_idx
            order_idx += 1
        else:
            priorities.append(priorities.popleft())
            pri_idx.append(pri_idx.popleft())

    return result_dic[location]

priorities = [2, 1, 3, 2]
location = 2

print(solution(priorities, location))