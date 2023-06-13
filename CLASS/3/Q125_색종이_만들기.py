#https://www.acmicpc.net/problem/2630
#문제 125 - 색종이 만들기

# ver_1.0
import sys
input = sys.stdin.readline

w_cnt, b_cnt = 0, 0
def cut_paper(x, y, N, lst):
    global w_cnt, b_cnt
    tmp_cnt = 0
    for i in range(x, x + N):
        for j in range(y, y + N):
            if lst[i][j]:
                tmp_cnt += 1
    if not tmp_cnt:
        w_cnt += 1
    elif tmp_cnt == N**2:
        b_cnt += 1
    else:
        cut_paper(x, y, N // 2, lst)
        cut_paper(x + N // 2, y, N // 2, lst)
        cut_paper(x, y + N // 2, N // 2, lst)
        cut_paper(x + N // 2, y + N // 2, N // 2, lst)

n = int(input())
nlist = []
for _ in range(n):
    nlist.append(list(map(int, input().split())))
cut_paper(0,0,n,nlist)
print(w_cnt)
print(b_cnt)
