import sys

num_H, num_M = map(int, sys.stdin.readline().split())
num_D = (num_H*60)+num_M - 45
if (num_D//60) < 0 :
    print((num_D//60)+24 , num_D%60)
else :
    print(num_D//60  , num_D%60)


# H, M = map(int, sys.stdin.readline().split())
# if M < 45 :
#     if H == 0 :
#         H = 23
#         M += 60
#     else :
#         H -= 1
#         M += 60
# print(H, M-45)