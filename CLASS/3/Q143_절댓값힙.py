# https://www.acmicpc.net/problem/11286
# 문제 143 - 절댓값 힙

# # ver_1.0
# # 리스트로 구현하다가 시간초과날듯 싶어서 포기
# import sys
# input = sys.stdin.readline

# N = int(input())
# x_plus_list = []
# x_minus_list = []
# for _ in range(N):
#     x = int(input())
#     if x != 0:
#         if x > 0:
#             x_plus_list.append(x)
#         else:
#             x_minus_list.append(x)
#     else:
#         if x_plus_list or x_minus_list:
#             # x_plus_list 와 x_minus_list에서 
#             # 절대값이 제일 작은 수를
#             # 리스트에서 제거 후 출력
#             pass
#         else:
#             print(0)

# ver_2.0
# heapq를 사용하여 구현
import sys
import heapq

input = sys.stdin.readline

N = int(input())
x_heap = []

for _ in range(N):
    x = int(input())
    if x != 0:
        #절댓값x,x를 튜플형태로 힙에 저장
        heapq.heappush(x_heap, (abs(x), x))
    else:
        if x_heap:
            #절댓값x,x를 꺼냄 (제일 작은 수)
            _, min_x = heapq.heappop(x_heap)
            print(min_x)
        else:
            print(0)
