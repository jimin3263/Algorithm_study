k = 80
dungeons = [[80,20],[50,40],[30,10]]

import itertools
def solution(k, dungeons):
    answer = 0
    for dungeon in itertools.permutations(dungeons):
        temp_cnt = 0
        temp_k = k
        for need, use in dungeon:
            if (need <= temp_k):
                temp_k -= use
                temp_cnt += 1
        answer = max(temp_cnt, answer)
    return answer

print(solution(k, dungeons))