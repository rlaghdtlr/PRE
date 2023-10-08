# https://www.acmicpc.net/problem/16928
# 문제 147 - 뱀과 사다리 게임

# # ver_1.0
# from collections import deque
# import sys
# input = sys.stdin.readline

# def game(ladder, snake):
#     board = [0]*101
#     visited = [False]*101

#     #첫 번째 좌표부터 시작
#     q = deque([1])

#     while q:
#         i = q.popleft()

#         if i == 100:
#             return board[i]
#         for dice in range(1,7):
#             next_place = i + dice
#             if next_place <= 100 and not visited[next_place]:
#                 # 움직이는 지역에 사다리 존재
#                 if next_place in ladder.keys():
#                     next_place = ladder[next_place]
#                 # 뱀 존재
#                 if next_place in snake.keys():
#                     next_place = snake[next_place]
#                 # 아무것도 없음
#                 if not visited[next_place]:
#                     visited[next_place] = True
#                     board[next_place] = board[i] + 1
#                     q.append(next_place)

# ladder = dict()
# snake = dict()

# n, m = map(int, input().split())

# for _ in range(n):
#     a, b = map(int, input().split())
#     ladder[a] = b
# for _ in range(m):
#     a, b = map(int, input().split())
#     snake[a] = b

# print(game(ladder,snake))

# 경우의 수를 구하는 것 최소의 주사위 리롤로 100에 도달하여야 한다 그때의 최소 리롤 횟수 출력
# 나는 1~6까지 전진 가능
# 사다리를 타면 그 쪽으로 이동 (높아짐)
# 뱀을 타면 그 쪽으로 이동 (낮아짐)
# 각 1번부터 100번까지 몇 번 움직일 수 있는지 기록해놓고 100번에 기록된 수를 출력하면 끝

# ver_2.0
# visited 리스트 사용 안하고 구현
from collections import deque
import sys
input = sys.stdin.readline

def game(ladder, snake):
    board = [-1]*101

    #첫 번째 좌표부터 시작
    q = deque([1])
    board[1] = 0

    while q:
        i = q.popleft()

        if i == 100:
            return board[i]
        for dice in range(1,7):
            next_place = i + dice
            if next_place <= 100 and board[next_place] == -1:
                # 움직이는 지역에 사다리 존재
                if next_place in ladder.keys():
                    next_place = ladder[next_place]
                # 뱀 존재
                if next_place in snake.keys():
                    next_place = snake[next_place]
                # 아무것도 없음
                if board[next_place] == -1:
                    board[next_place] = board[i] + 1
                    q.append(next_place)

ladder = dict()
snake = dict()

n, m = map(int, input().split())

for _ in range(n):
    a, b = map(int, input().split())
    ladder[a] = b
for _ in range(m):
    a, b = map(int, input().split())
    snake[a] = b

print(game(ladder,snake))