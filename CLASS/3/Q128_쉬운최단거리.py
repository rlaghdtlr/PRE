# https://www.acmicpc.net/problem/14940
# 문제 128 - 쉬운 최단거리

# ver_1.0
from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
map_data = []
for _ in range(n):
    map_data.append(list(map(int, input().split())))

# 목표지점의 좌표 찾기
target_row, target_col = None, None
for i in range(n):
    for j in range(m):
        if map_data[i][j] == 2:
            target_row, target_col = i, j
            break

# 방향 설정 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 최단 거리 저장을 위한 2차원 배열
distances = [[-1] * m for _ in range(n)]

# BFS 탐색을 위한 큐
queue = deque([(target_row, target_col)])
distances[target_row][target_col] = 0  # 목표지점의 거리는 0으로 설정

while queue:
    x, y = queue.popleft()

    # 상하좌우 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위를 벗어나는 경우 무시
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        # 갈 수 없는 땅이거나 이미 방문한 경우 무시
        if map_data[nx][ny] == 0 or distances[nx][ny] != -1:
            continue

        # 새로운 지점까지의 거리 갱신
        distances[nx][ny] = distances[x][y] + 1
        queue.append((nx, ny))

# 결과 출력
for i in range(n):
    for j in range(m):
        if map_data[i][j] == 0:
            print(0, end=' ')
        else:
            print(distances[i][j], end=' ')
    print()


# ver_2.0
# 코드 간결화
from collections import deque
from sys import stdin

rd = stdin.readline

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

n, m = map(int, rd().rstrip().split())
MAP = []
target = ()

for row in range(m):
    line = list(map(int, rd().rstrip().replace('1', '-1').split()))
    if 2 in line:
        target = (row, line.index(2))
        line[line.index(2)] = 0
    MAP.append(line)

q = deque([target])

while q:
    r, c = q.popleft()
    for mv_idx in range(4):
        nr = r + dr[mv_idx]
        nc = c + dc[mv_idx]
        if 0 <= nr < n and 0<= nc < m and MAP[nr][nc] == -1:
            MAP[nr][nc] = MAP[r][c] + 1
            q.append((nr, nc))

for line in MAP:
    print(' '.join(list(map(str, line))))
