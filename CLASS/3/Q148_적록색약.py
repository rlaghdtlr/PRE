# https://www.acmicpc.net/problem/10026
# 문제 148 - 적록색약

# ver_1.0
# 오답
# 방문 리스트에 일반일경우 색약일경우를 각각 기록하여 출력
from collections import deque
import sys
input = sys.stdin.readline

def area(li,n):
    visited1 = [[0] * n for _ in range(n)]
    visited2 = [[0] * n for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    cnt1 = 0
    cnt2 = 0
    for i in range(n):
        for j in range(n):
            if visited1[i][j] == 0:
                cnt1 += 1
                q.append((i,j))
                while q:
                    x, y = q.popleft()

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if nx < 0 or nx >=n or ny < 0 or ny >=n:
                            continue
                        if li[x][y] == li[nx][ny] and visited1[nx][ny] == 0:
                            visited1[nx][ny] = cnt1
                            q.append((nx,ny))
            elif visited2[i][j] == 0:
                cnt2 += 1
                q.append((i,j))
                while q:
                    x, y = q.popleft()

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if nx < 0 or nx >=n or ny < 0 or ny >=n:
                            continue
                        if visited2[nx][ny] == 0:
                            if (li[x][y] == 'R' or li[x][y] == 'G') and (li[nx][ny] == 'R' or li[nx][ny] == 'G'):
                                visited2[nx][ny] = cnt1
                                q.append((nx,ny))
                            elif (li[x][y] == 'B' and li[nx][ny] == 'B'):
                                visited2[nx][ny] = cnt1
                                q.append((nx,ny))
    print(cnt1, cnt2)


painting = []
n = int(input())
for _ in range(n):
    painting.append(input().rstrip())
area(painting,n)


# ver_2.0
# 코드 개선 정답
# 일반 사람일때 값을 먼저 구한 후 리스트를 수정하여 다시 값을 구함
from collections import deque
import sys
input = sys.stdin.readline

def area(li,n):
    visited = [[0] * n for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                cnt += 1
                q.append((i,j))
                while q:
                    x, y = q.popleft()

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if nx < 0 or nx >=n or ny < 0 or ny >=n:
                            continue
                        if li[x][y] == li[nx][ny] and visited[nx][ny] == 0:
                            visited[nx][ny] = cnt
                            q.append((nx,ny))
    return cnt

painting = []
n = int(input())
for _ in range(n):
    painting.append(list(input().rstrip()))
nomal = area(painting,n)
for i in range(n):
    for j in range(n):
        if painting[i][j] == 'R':
            painting[i][j] = 'G'
change = area(painting,n)
print(nomal, change)