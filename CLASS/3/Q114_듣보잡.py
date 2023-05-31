#https://www.acmicpc.net/problem/1764
#문제 114 - 듣보잡

# ver 1.0
# 오답원인 시간초과
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nlist = []
nmlist = []
for i in range(n):
    nlist.append(input().rstrip())
for _ in range(m):
    man = input().rstrip()
    if man in nlist:
        nmlist.append(man)
print(len(nmlist))
print(*nmlist, sep='\n')

# ver 2.0
# set을 사용하여 중복값 제거로 시간복잡도 개선
# 사전순으로 출력을 위해 정렬
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nset = set()
nmlist = []
for i in range(n):
    nset.add(input().rstrip())
for _ in range(m):
    man = input().rstrip()
    if man in nset:
        nmlist.append(man)
print(len(nmlist))
print(*sorted(nmlist), sep='\n')