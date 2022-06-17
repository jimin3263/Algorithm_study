def solution(clothes):
    clothes_dict = dict()
    for i in range(len(clothes)):
        if (clothes[i][1] in clothes_dict.keys()):
            clothes_dict[clothes[i][1]] += 1
        else:
            clothes_dict[clothes[i][1]] = 1

    answer = 1
    for key in clothes_dict:
        answer *= (clothes_dict[key] + 1)
    return answer - 1

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))
