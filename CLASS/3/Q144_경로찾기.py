# https://www.acmicpc.net/problem/11403
# 문제 144 - 경로찾기

# # ver_1.0
# # 알고리즘 파악 실패
# import sys
# input = sys.stdin.readline
# nlist = []
# N = int(input())
# for _ in range(N):
#     nlist.append(list(map(int, input().split())))
# print(nlist)
# for i in range(N):
#     for j in range(N):
#         if nlist[i][j] == 1 and nlist[j][i] == 1:
#             nlist[i][j] = 0
#         else:
#             nlist[i][j] = 1
# print('result')
# print(nlist)

# ver_2.0
# 플로이드 와샬 알고리즘 - 모든 노드 쌍 간의 최단 경로를 찾을 때 사용
import sys
input = sys.stdin.readline
nlist = []
N = int(input())
for _ in range(N):
    nlist.append(list(map(int, input().split())))
for k in range(N):
    for i in range(N):
        for j in range(N):
            if nlist[i][k] == 1 and nlist[k][j] == 1:
                nlist[i][j] = 1
for i in nlist:
    print(' '.join(map(str, i)))