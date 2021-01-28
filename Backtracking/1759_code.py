L,C = map(int,input().split())
eng_list = list(input().split())
eng_list=sorted(eng_list)

result = []

#알파벳 체크
check=[False]*C

def back(count,check,result,d):
    vowel = ['a','e','i','o','u']
    #모음 체크
    if (L==count):
        count =0
        for i in result:
            if i in vowel:
                count+=1
        #count: 모음 갯수, L-count: 자음 갯수
        if count > 0 and L-count>1:
            for i in result:
                print(i,end='')
            print()
        return

    for i in range(d,C):
        if check[i]:
            continue
        result.append(eng_list[i])
        check[i] = True
        back(count+1,check,result,i+1)
        check[i] = False
        result.pop()


back(0,check,result,0)
