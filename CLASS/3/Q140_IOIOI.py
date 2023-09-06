# https://www.acmicpc.net/problem/5525
# 문제 140 - IOIOI

# # ver_1.0
# import sys
# input = sys.stdin.readline

# n = int(input())
# m = int(input())
# s = input().strip()

# pattern = ("IO"*n + "I")

# count = 0
# i = 0

# while i < m - len(pattern) + 1:
#     if s[i:i+len(pattern)] == pattern:
#         count += 1
#         i += 1  # 다음 위치로 이동
#     else:
#         i += 1

# print(count)

# # ver_2.0 코드 최적화
# import sys
# input = sys.stdin.readline

# n = int(input())
# m = int(input())
# s = input().strip()

# pattern = ("IO" * n + "I")
# pattern_len = len(pattern)

# count = 0
# i = 0

# while i < m - pattern_len + 1:
#     if s[i:i+pattern_len] == pattern:
#         count += 1
#         i += 1
#     else:
#         i += 1

# print(count)

# ver_3.0 완전최적화
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()

answer, i, count = 0, 0, 0

while i < (m - 1):
    # 문자열 3개를 읽어서 'IOI'가 나오는 경우
    if s[i:i+3] == 'IOI':
        # 오른쪽으로 2칸 이동
        i += 2
        # 반복수 추가
        count += 1
        # 반복수가 찾는 문자열의 반복수와 같으면
        if count == n:
            # 찾는 문자열 개수 추가
            answer += 1
            # 반복수 빼기
            count -= 1
    else:
        # 오른쪽으로 1칸 이동
        i += 1
        count = 0

print(answer)
