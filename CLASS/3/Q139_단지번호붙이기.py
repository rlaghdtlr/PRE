# https://www.acmicpc.net/problem/2667
# 문제 139 - 단지번호 붙이기

# # ver_1.0
# from collections import deque

# def bfs(grid, row, col, visited):
#     # 시작좌표
#     queue = deque([(row, col)])
#     visited[row][col] = True
#     # 주택개수 시작 주택부터 1
#     count = 1

#     while queue:
#         r, c = queue.popleft()

#         # 근처 탐색시작
#         directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#         for dr, dc in directions:
#             nr, nc = r + dr, c + dc
#             if (
#                 0 <= nr < len(grid)
#                 and 0 <= nc < len(grid[0])
#                 and grid[nr][nc] == 1
#                 and not visited[nr][nc]
#             ):
#                 queue.append((nr, nc))
#                 visited[nr][nc] = True
#                 count += 1

#     return count

# # 메인
# import sys
# input = sys.stdin.readline

# n = int(input())

# nlist = []
# house = []
# visited = [[False] * n for _ in range(n)]

# for _ in range(n):
#     nlist.append(list(map(int, input().strip())))

# for row in range(n):
#     for col in range(n):
#         if nlist[row][col] == 1 and not visited[row][col]:
#             house.append(bfs(nlist, row, col, visited))

# print(len(house))
# print("\n".join(map(str, sorted(house))))


# ver_2.0
# 메인함수 간소화 버전
from collections import deque

def bfs(list, n):
    houses = []
    visited = [[False] * n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            if nlist[row][col] == 1 and not visited[row][col]:
                # 시작좌표
                queue = deque([(row, col)])
                visited[row][col] = True
                # 시작 주택부터 1개
                count = 1

                while queue:
                    r, c = queue.popleft()
                    # 주택근처 탐색시작
                    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if (
                            0 <= nr < n
                            and 0 <= nc < n
                            and list[nr][nc] == 1
                            and not visited[nr][nc]
                        ):
                            queue.append((nr, nc))
                            visited[nr][nc] = True
                            count += 1
                houses.append(count)
    return houses

# 메인
import sys
input = sys.stdin.readline

n = int(input())
nlist = []
for _ in range(n):
    nlist.append(list(map(int, input().strip())))

house = bfs(nlist, n)

print(len(house))
print("\n".join(map(str, sorted(house))))
# 단지수 출력
# 각 단지별 집 수 오름차순 정렬 출력

