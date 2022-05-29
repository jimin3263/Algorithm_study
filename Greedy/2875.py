#2875
n,m,k = map(int,input().split())

team_count= 0
while (n >= 2 and m >= 1 and (n + m) - 3 >= k ):
    n -= 2
    m -= 1
    team_count += 1

print(team_count)
