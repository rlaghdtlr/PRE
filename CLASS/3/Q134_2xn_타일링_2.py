# https://www.acmicpc.net/problem/11727
# 문제 134 - 2xn 타일링 2

# ver_1.0
n = int(input())
nlist = [1,3]
for i in range(2,n):
    nlist.append((nlist[i-1]+nlist[i-2]*2)%10007)

print(nlist[n-1])

# 1 3 5 11 21 43 85 171
# 1 (1+1*2) (3+1*2) (5+3*2) ....