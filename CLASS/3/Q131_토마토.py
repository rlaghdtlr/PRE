# https://www.acmicpc.net/problem/7576
# 문제 131 - 토마토

# ver_1.0
import sys
input = sys.stdin.readline
from collections import deque

def tomato_riping(box):
    # 방향 설정 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 상자의 크기
    rows = len(box)
    cols = len(box[0])

    # 익은 토마토의 좌표를 큐에 저장
    queue = deque()
    for i in range(rows):
        for j in range(cols):
            if box[i][j] == 1:
                queue.append((i, j))

    # BFS 탐색 시작
    days = -1  # 초기 일수는 -1로 설정 (탐색 전에 1일이 지난 것으로 간주)
    while queue:
        size = len(queue)

        # 같은 날짜에 익게 되는 토마토들을 모두 처리
        for _ in range(size):
            x, y = queue.popleft()

            # 인접한 익지 않은 토마토를 익게 만듦
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                # 범위를 벗어나는 경우 무시
                if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                    continue

                # 익지 않은 토마토인 경우 익게 만들고 큐에 추가
                if box[nx][ny] == 0:
                    box[nx][ny] = 1
                    queue.append((nx, ny))
                    
        days += 1

    # 모든 토마토가 익었는지 확인
    for i in range(rows):
        for j in range(cols):
            if box[i][j] == 0:
                return -1  # 익지 않은 토마토가 남아있는 경우

    return days if days >= 0 else 0  # 초기에 모든 토마토가 익은 경우 0 반환


m, n = map(int,input().split())
box = [list(map(int, input().split())) for _ in range(n)]
print(tomato_riping(box))