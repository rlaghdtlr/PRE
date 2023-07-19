# https://www.acmicpc.net/problem/2178
# 문제 137 - 미로 탐색

# ver_1.0
import sys
input = sys.stdin.readline
from collections import deque

def bfs(i, j):
    dxy = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    distance[i][j] = 0  # 시작 지점의 이동 거리는 0

    while q:
        x, y = q.popleft()

        # 방향 설정
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and map[nx][ny] == "1":
                visited[nx][ny] = 1
                distance[nx][ny] = distance[x][y] + 1
                q.append((nx, ny))

n, m = map(int, input().split())
map = [list(str(input().strip())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
distance = [[0] * m for _ in range(n)]

bfs(0, 0)

print(distance[n-1][m-1]+1)  # (n-1, m-1)까지의 최소 이동 거리 출력


# ver_2.0 코드개선
import sys
input = sys.stdin.readline
from collections import deque

def bfs(i, j):
    dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q = deque()

    # 시작점
    q.append((0, 0))
    # 시작거리
    distance[0][0] = 1

    while q:
        x, y = q.popleft()

        # 방향 설정
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m and not distance[nx][ny] and map[nx][ny] == "1":
                distance[nx][ny] = distance[x][y] + 1
                q.append((nx, ny))

    return distance[i-1][j-1]

n, m = map(int, input().split())
map = [list(str(input().strip())) for _ in range(n)]
distance = [[0] * m for _ in range(n)]

print(bfs(n, m))
