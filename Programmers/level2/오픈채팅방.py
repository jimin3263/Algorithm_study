def solution(record):
    answer = []
    check_list = []
    nickname = dict()

    for rec in record:
        arr = rec.split(" ")
        check_list.append(arr)
        if (arr[0] == 'Enter' or arr[0] == 'Change'):
            nickname[arr[1]] = arr[2]

    for check in check_list:
        if (check[0] == 'Enter'):
            answer.append(nickname[check[1]]+"님이 들어왔습니다.")
        elif(check[0] == 'Leave'):
            answer.append(nickname[check[1]]+"님이 나갔습니다.")
    return answer
