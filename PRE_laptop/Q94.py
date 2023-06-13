# a, b, v = map(int, input().split())
# top = 0
# day = 1
# while True:
#     top += a
#     if top >= v:
#         break
#     top -= b
#     day += 1
# print(day)

import math

a, b, v = map(int, input().split())
days = math.ceil((v-b)/(a-b))
print(days)
