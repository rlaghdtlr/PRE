# import sys
# input = sys.stdin.readline
# n = int(input())
# nlist = {}

# for _ in range(n):
#     m = int(input())
#     if m in nlist:
#         nlist[m] += 1
#     else:
#         nlist[m] = 1
# sortlist = sorted(nlist.keys())
# for i in sortlist:
#     value = nlist[i]
#     for j in range(value):
#         print(i)

# import sys
# input = sys.stdin.readline
# n = int(input())
# nlist = []

# for _ in range(n):
#     m = int(input())
#     nlist.append(m)

# sortlist = sorted(set(nlist))

# for i in sortlist:
#     count = nlist.count(i)
#     for j in range(count):
#         print(i)

import sys
input = sys.stdin.readline
n = int(input())
nlist = [0]*10001
for _ in range(n):
    nlist[int(input())] += 1
for i in range(len(nlist)):
    if nlist[i] != 0:
        for _ in range(nlist[i]):
            print(i)