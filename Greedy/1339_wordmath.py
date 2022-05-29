n= int(input())
word=[]
for i in range(n):
    word.append(input())

dic ={}
    
#ABC일 경우 A=100 B=10 C=1

for i in range(len(word)):
    for j in range(len(word[i])):
        if word[i][j] not in dic:
            dic[word[i][j]] = pow(10,len(word[i])-(j+1))
        else:
            dic[word[i][j]] += pow(10,len(word[i])-(j+1))
            
#딕셔너리를 활용하여 내림차순으로 정렬 후 큰 수부터 9~0 숫자 대입
dic_sorted = sorted(dic.items(),reverse=True,key=lambda item:item[1])

mult = 9
result= 0
for key,value in dic_sorted:
    result += mult*value
    mult-=1

print(result)
