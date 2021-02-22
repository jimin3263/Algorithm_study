T = input()
P = input()

# 불일치 발생하면 돌아갈 인덱스 지정
def KMP_preprocess():
    next = [0] * len(P)
    j = 0
    for i in range(1, len(P)):
        while (j > 0 and P[i] != P[j]):
            j = next[j - 1]
        if (P[i] == P[j]):
            j += 1
            next[i] = j
    return next

cnt=0
# KMP algorithm
def KMP(next):
    N=len(T);M=len(P)
    j=0
    pos=[]
    global cnt
    for i in range(N):
        while j>0 and T[i]!=P[j]:
            j=next[j-1]
        if T[i]==P[j]:
            if j==(M-1):
                cnt+=1
                pos.append(i+1-(len(P)-1))
                j=next[j]
            else:
                j+=1
    return pos

table= KMP_preprocess()
num=KMP(table)
print(cnt)
print(*num)
