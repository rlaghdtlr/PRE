# n, m = map(int, input().split())
# maxnum = max(n,m)
# while maxnum>0:
#     if n%maxnum ==0 and m%maxnum == 0:
#         break
#     else:
#         maxnum -= 1
# print(maxnum)
# print(int(n*m/maxnum))

n, m = map(int, input().split())

num = min(n, m)
while num > 0 and (n % num != 0 or m % num != 0):
    num -= 1

print(num)
print(n * m // num)

