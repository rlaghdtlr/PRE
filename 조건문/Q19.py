import sys

num_H, num_M = map(int, sys.stdin.readline().split())
num_T = int(sys.stdin.readline())
num_D = (num_H*60)+num_M + num_T
if (num_D//60) < 0 :
    print((num_D//60)+24 , num_D%60)
elif (num_D//60) >=24 :
    print((num_D//60)-24 , num_D%60)
else :
    print(num_D//60 , num_D%60)


# H, M = map(int, input().split())
# T = int(input())

# if (M+T)//60 > 0 :
#     H = H+(M+T)//60
#     M = (M+T)%60
# else :
#     M = M+T
# if H//24 > 0:
#     H = H%24

# print(H, M)
