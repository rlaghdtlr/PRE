# https://www.acmicpc.net/problem/6064
# 문제 141 - 카잉 달력

# # ver_1.0
# # 시간초과
# import sys
# import math
# input = sys.stdin.readline


# def kaing(m,n,x,y):
#     max = math.lcm(m, n)
#     year = 1
#     i = 1
#     j = 1
#     while(1):
#         if i == x and j == y:
#             break
#         if i >= m:
#             i = 0
#         if j >= n:
#             j = 0
#         if year > max:
#             return -1
#         i = i+1
#         j = j+1
#         year = year+1
#     return year

# t = int(input())
# for _ in range(t):
#     m,n,x,y = map(int, input().split())
#     print(kaing(m,n,x,y))

# ver_2.0
import sys
input = sys.stdin.readline

def kaing(m,n,x,y):
    cnt = x #k를 x로 초기화
    while cnt <= m * n: #k의 범위는 m*n을 넘을 수 없기에
        if (cnt - x) % m == 0 and (cnt - y) % n == 0: #2개의 조건을 만족하는 k값을 찾는다.
            return cnt
        cnt += m #k-x가 m의 배수이기 때문에 k는 x로 초기화해주었기 때문에 m만 더해준다.
    return -1

t = int(input())
for _ in range(t):
    m,n,x,y = map(int, input().split())
    print(kaing(m,n,x,y))