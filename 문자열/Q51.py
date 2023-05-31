# S = input()
# timer = 0
# for i in S:
#     n = ord(i)
#     if 24>=n>=18:
#         timer += (n-1)//3+3
# print(timer)
# 숫자를 다 더하고 숫자 개수만큼 수를 더함 ex) 5293 은 5+2+9+3 + 4 해서 23


S = input()
timer = 0
for i in S:
    n = ord(i) - 65 # S : 18/ Z = 25
    if(24 >= n >= 18):
        timer += (n-1)//3
    elif(n == 25):
        timer += (n-2)//3   
    else:
        timer += n//3
    timer += 3
print(timer)
