def solution(s):
    answer = float("inf")
    if (len(s) == 1):
        return 1

    for i in range(1, len(s)//2 +1): #길이
        s1 = s[0:i] #처음 비교
        cnt = 1
        result = ''
        for j in range(i, len(s), i): #찐 문자열
            if (s1 == s[j:j+i]):
                cnt += 1
            else: 
                if (cnt == 1):
                    result += s1
                else:
                    result += str(cnt) + s1
                
                cnt = 1 #압축 갯수
                s1 = s[j:j+i]
        
        if(cnt == 1):
            result += s1
        else:
            result += str(cnt) + s1
        answer = min(answer,len(result))
            
        
    return answer
