# https://www.acmicpc.net/problem/9461
# 문제 133 - 파도반 수열

# ver_1.0
nlist = [0]
for i in range(1,101):
    if i == 1 or i == 2 or i == 3:
        nlist.append(1)
    else:
        nlist.append(nlist[i-2] + nlist[i-3])

T = int(input())
for _ in range(T):
    n = int(input())
    print(nlist[n])

# ver_2.0 코드 간소화
nlist = [1,1,1]
for i in range(3,101):
    nlist.append(nlist[i-2]+nlist[i-3])
T = int(input())
for _ in range(T):
    print(nlist[int(input())-1])