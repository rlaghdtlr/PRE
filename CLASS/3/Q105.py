T = int(input())

Nlist = [[1,0],[0,1]]
N = []
for _ in range(T):
    N.append(int(input()))
for i in range(2, max(N)+1):
    Nlist.append([0,0])
    for j in range(2):
        Nlist[i][j] = int(Nlist[i-1][j])+int(Nlist[i-2][j])
for i in N:
    print(*Nlist[i],end='\n')



# for i in N:
# if N <2:
#     print(*Nlist[N])
# else:
#     print(*Nlist[N-2]+Nlist[N-1])


# 0 = 1 0
# 1 = 0 1
# 2 = 1 1
# 3 = 1 2
# 4 = 2 3
# 5 = 3 5
# 6 = 5 8
