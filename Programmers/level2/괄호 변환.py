
#균형잡힌 괄호 문자열 -> ( ) 개수가 같은 경우
#올바른 괄호 문자열 -> 짝이 맞는 경우

#p = ")("
p = "()))((()"
def check_right_string(u): #올바른 문자열
    check_stack = []
    for i in range(len(u)):
        if (u[i] == "("):
            check_stack.append(u[i])
        elif (u[i] == ")"):
            if (len(check_stack) > 0 and check_stack[-1] == "("):
                check_stack.pop()

    if(len(check_stack) == 0):
        return True
    else:
        return False

def divide(p):
    left_bracket, right_bracket = 0,0
    for i in range(len(p)):
        if (p[i] == "("):
            left_bracket += 1
        elif (p[i] == ")"):
            right_bracket += 1
        if (left_bracket == right_bracket): #같다면 쪼개기
            return p[:i+1], p[i+1:]


def solution(p):
    if (p ==""): #1. 빈문자열인 경우 빈 문자열 반환
        return ""
    u,v = divide(p)
    if(check_right_string(u)): #올바른 문자열이라면 v에 대해서 다시 수행
        return u + solution(v)
    else:
        answer = "("
        answer += solution(v)
        answer += ")"
        u = u[1:len(u)-1]
        for i in range(len(u)):
            if (u[i] == "("):
                str = ")"
            else:
                str = "("
            answer += str
        return answer

print(solution(p))