# https://www.acmicpc.net/problem/9375
# 문제 132 - 패션왕 신해빈

# ver_1.0 딕셔너리에 리스트를 사용
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    wear = {}
    a = int(input())
    for _ in range(a):
        name, ty = map(str, input().split())
        if ty in wear:
            wear[ty].append(name)
        else:
            wear[ty] = [name]

    # print(wear)
    # count_ty = 0
    # count = 0
    # for value in wear.values():
    #     count_ty += 1
    #     count += len(value)
    # print('가지 수 =',count_ty)
    # print('모든 값의 개수 =',count)

    ccount = 1
    for value in wear.values():
        ccount *= len(value) + 1
    print(ccount-1)
    # print('조합 수 =',ccount)

# ver_2.0 리스트에 딕셔너리를 사용
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    wear = []
    a = int(input())
    for _ in range(a):
        name, ty = map(str, input().split())
        wear.append(ty)

    type_counts = {}
    for ty in wear:
        if ty in type_counts:
            type_counts[ty] += 1
        else:
            type_counts[ty] = 1

    ccount = 1
    for count in type_counts.values():
        ccount *= (count + 1)
    print(ccount - 1)

# # ver_3.0 리스트로만 구현 실패
# import sys
# input = sys.stdin.readline

# n = int(input())
# for _ in range(n):
#     wear = []
#     a = int(input())
#     for _ in range(a):
#         name, ty = map(str, input().split())
#         wear.append(ty)
#     type_counts = [0] * (max(wear) + 1)  # 종류별 개수를 저장할 리스트 초기화

#     for ty in wear:
#         type_counts[ty] += 1

#     ccount = 1
#     for count in type_counts:
#         ccount *= (count + 1)
#     print(ccount - 1)