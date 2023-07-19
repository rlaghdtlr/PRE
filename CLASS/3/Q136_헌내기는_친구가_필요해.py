# https://www.acmicpc.net/problem/21736
# 문제 136 - 헌내기는 친구가 필요해

# ver_1.0
from collections import deque

def find_friend(classroom, mypoint):
    # 방향 설정 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 공간의 크기
    rows = len(classroom)
    cols = len(classroom[0])

    # 내 위치를 큐에 저장
    queue = deque()
    queue.append(mypoint)

    # 방문한 위치 기록
    visited = set()
    visited.add(mypoint)

    # BFS 탐색 시작
    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            # 범위를 벗어나거나 이미 방문한 위치인 경우 무시
            if nx < 0 or nx >= rows or ny < 0 or ny >= cols or (nx, ny) in visited:
                continue

            # 새로운 공간을 체크하고 큐에 추가
            if classroom[nx][ny] == 0:
                classroom[nx][ny] = 1
                queue.append((nx, ny))
                visited.add((nx, ny))
            # 사람을 만나면 만났다고 표시하고 큐에 추가
            elif classroom[nx][ny] == 3:
                classroom[nx][ny] = 4
                queue.append((nx, ny))
                visited.add((nx, ny))

    # 사람을 얼마나 만났는지 확인
    cnt = 0
    for i in range(rows):
        for j in range(cols):
            # 만난 사람의 수 세기
            if classroom[i][j] == 4:
                cnt += 1

    if cnt == 0:
        return 'TT'
    else:
        return cnt

# 입력
n, m = map(int, input().split())
classroom = []

for i in range(n):
    S = input().rstrip()
    if 'I' in S:
        mypoint = (i, S.index("I"))
    # 내 위치는 2, 벽은 -1, 사람은 3, 공간은 0으로 표시
    new_list = [2 if item == "I" else -1 if item == "X" else 3 if item == "P" else 0 for item in list(S)]
    classroom.append(new_list)
print(find_friend(classroom, mypoint))


# ver_2.0 코드 간소화
import sys
input = sys.stdin.readline
from collections import deque

def find_friend(i, j):
    cnt = 0
    q = deque()
    q.append([i, j])
    visited[i][j] = 1
    dxy = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    while q:
        x, y = q.popleft()

        # 방향 설정
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = 1
                if classroom[nx][ny] == "O" or classroom[nx][ny] == "P":
                    q.append([nx, ny])
                    if classroom[nx][ny] == "P":
                        cnt += 1

    return cnt if cnt != 0 else "TT"

n, m = map(int, input().split())
classroom = [list(str(input().strip())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if classroom[i][j] == "I":
            print(find_friend(i, j))
            exit()
