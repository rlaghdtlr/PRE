import sys
input = sys.stdin.readline

stu = [i for i in range(1,31)]
for _ in range (28):
    n = int(input())
    stu[n-1] = 0
stu.sort()
print(stu[28])
print(stu[29])

# stu = []
# bignum = []

# for _ in range (28):
#     stu.append(int(input()))

# for i in range (1, 31):
#     try:
#         stu.index(i)
#     except:
#         bignum.append(i)
# print(min(bignum))
# print(max(bignum))

