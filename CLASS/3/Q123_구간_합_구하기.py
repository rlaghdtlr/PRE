#https://www.acmicpc.net/problem/11659
#문제 123 - 구간 합 구하기


# ver_1.0
# 시간초과
import sys
input = sys.stdin.readline


def sum_nlist_num(num, list, xnum, ynum):
    count = 0
    for i in range (num):
        if xnum<= (i+1) <= ynum:
            count += list[i]
    return count
n, m = map(int, input().split())
nlist = list(map(int, input().split()))
for _ in range(m):
    x, y = map(int, input().split())
    print(sum_nlist_num(n, nlist, x, y))

# ver_2.0
# 시간복잡도 로직 수정
import sys
input = sys.stdin.readline


def sum_nlist_num(list, x, y):
    return list[y] - list[x-1]

n, m = map(int, input().split())
nlist = list(map(int, input().split()))
sumlist = [0]  # 누적 합을 저장할 리스트

for i in range(n):
    sumlist.append(sumlist[-1] + nlist[i])

for _ in range(m):
    a, b = map(int, input().split())
    print(sum_nlist_num(sumlist, a, b))

