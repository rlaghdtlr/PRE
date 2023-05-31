# N = int(input())
# M = int(input())
# button = [i for i in range(10)]
# if M != 0:
#     Mlist = list(map(int, input().split()))
# else:
#     Mlist = []
# #목표채널
# target = [int(i) for i in str(N)]
# #사용 가능한 버튼 리스트
# button = list(set(button) - set(Mlist))
# #버튼 누른 횟수
# count = 0
# #시작 채널
# start = 100
# newtarget = []
# if start != N:
#     for i in target:
#         close = button[0]
#         for j in button:
#             if j == i:
#                 newtarget.append(j)
#                 count+=1
#                 break
#             elif abs(i - j) < abs(close - j):
#                 close = j
#         else:
#             newtarget.append(close)
#             count+=1
#     else:
#         count += abs(int(''.join(map(str, target))) - int(''.join(map(str, newtarget))))
# print(count)

N = int(input())
M = int(input())
if M != 0:
    button = set(range(10)) - set(map(int, input().split()))
else:
    button = set(range(10))

count = abs(N-100)
for i in range(1000000):
    for j in str(i):
        if int(j) not in button:
            break
    else:
        count = min(count, len(str(i)) + abs(i-N))

print(count)