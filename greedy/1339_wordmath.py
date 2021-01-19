n= int(input())
word=[]
dic ={}

for i in range(n):
    word.append(input())

for i in range(len(word)):
    for j in range(len(word[i])):
        if word[i][j] not in dic:
            dic[word[i][j]] = pow(10,len(word[i])-(j+1))
        else:
            dic[word[i][j]] += pow(10,len(word[i])-(j+1))

dic_sorted = sorted(dic.items(),reverse=True,key=lambda item:item[1])

mult = 9
result= 0

for key,value in dic_sorted:
    result += mult*value
    mult-=1

print(result)
