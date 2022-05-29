n= int(input())
rope = []
for i in range (n):
    rope.append(int(input()))
#오름차순으로 정렬할 경우, 그 다음 큰 로프가 무게를 견딜 수 없음
#내림차순으로 정렬
rope.sort(reverse=True)

k = []
for i in range (n):
    k.append((i+1)*rope[i])

#k 중에서 가장 큰 값 구함
print(max(k))
