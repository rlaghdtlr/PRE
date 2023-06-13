#https://www.acmicpc.net/problem/2630
#문제 125 - 색종이 만들기

# ver_1.0
import sys
input = sys.stdin.readline


def nlistcutcount(list, number):
    color = nlist[0][0]  # 현재 종이 영역의 색상

    # 현재 종이 영역에 있는 모든 정사각형이 같은 색인지 확인
    for i in range(row_start, row_end):
        for j in range(col_start, col_end):
            if paper[i][j] != color:
                # 같은 색이 아니라면 종이를 분할하여 재귀 호출
                half = (row_end - row_start) // 2
                return (
                    count_paper(paper, row_start, row_start + half, col_start, col_start + half) +
                    count_paper(paper, row_start, row_start + half, col_start + half, col_end) +
                    count_paper(paper, row_start + half, row_end, col_start, col_start + half) +
                    count_paper(paper, row_start + half, row_end, col_start + half, col_end)
                )

    # 현재 종이 영역에 있는 모든 정사각형이 같은 색인 경우
    return 1 if color == 1 else 0

n = int(input())
nlist = []
for _ in range(n):
    nlist.append(list(map(int, input().split())))

