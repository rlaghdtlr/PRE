# https://www.acmicpc.net/problem/5430
# 문제 145 - AC

# # ver_1.0
# # 출력형태때문에 두 번 틀림
# from collections import deque
# import sys
# input = sys.stdin.readline


# def AC (istr, inum, ilist):
#     ideque = deque(ilist)
#     reverse = 0
#     for i in istr:
#         if i == 'D':
#             if ideque:
#                 if reverse == 0:
#                     ideque.popleft()
#                 else:
#                     ideque.pop()
#             else:
#                 print('error')
#                 return 0
#         elif i == 'R':
#             if reverse == 0:
#                 reverse = 1
#             else:
#                 reverse = 0
#     if reverse == 1:
#         ideque.reverse()
#     print(str(list((ideque))).replace(' ', ''))
#     return 0

# T = int(input())
# for _ in range(T):
#     istr = input().strip()
#     inum = int(input())
#     # 입력받은 그대로 리스트로 저장
#     ilist = eval(input().strip())
#     AC(istr,inum,ilist)

# ver_2.0
# 입력부분 개선과 카운터를 사용하여 실행속도 개선
from collections import Counter, deque
import sys
input = sys.stdin.readline

def AC (istr, ilist):
    ideque = deque(list(ilist[1:-1].split(',')))
    reverse = True
    for i in istr:
        if i == 'R':
            reverse = not reverse
        else:
            if reverse:
                ideque.popleft()
            else:
                ideque.pop()
    if reverse:
        arr = list(ideque)
    else:
        arr = list(ideque)[::-1]
    print(f"[{','.join(arr)}]")

T = int(input())
for _ in range(T):
    istr = input().strip()
    inum = int(input())
    ilist = input().rstrip()
    if Counter(istr)['D'] > inum:
        print('error')
        continue
    if inum == 0:
        print('[]')
        continue
    AC(istr,ilist)