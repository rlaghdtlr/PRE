# https://www.acmicpc.net/problem/7569
# 문제 146 - 토마토

# ver_1.0
# 토마토를 익히는 큐를 돌린 후 나온 일 수를 출력하는 방법
# 모든 토마토를 익힐 수 있는 일 수를 구할 때 좋음
import sys
from collections import deque
input = sys.stdin.readline

def tomato_ripening(box,m,n,h):
    # 방향 설정 (상, 하, 좌, 우, 위, 아래)
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]


    # 익은 토마토의 좌표를 큐에 저장
    queue = deque()
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if box[i][j][k] == 1:
                    queue.append((k, j, i)) #x,y,z

    # 토마토가 있을 경우
    days = 0
    if queue:
        # BFS 탐색 시작
        while queue:
            size = len(queue)

            # 같은 날짜에 익게 되는 토마토들을 모두 처리
            for _ in range(size):
                x, y, z = queue.popleft()

                # 인접한 익지 않은 토마토를 익게 만듦
                for k in range(6):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    nz = z + dz[k]

                    # 범위를 벗어나는 경우 무시
                    if nx < 0 or nx >= m or ny < 0 or ny >= n or nz < 0 or nz >=h:
                        continue

                    # 익지 않은 토마토인 경우 익게 만들고 큐에 추가
                    if box[nz][ny][nx] == 0:
                        box[nz][ny][nx] = 1
                        queue.append((nx, ny, nz))
            days = days + 1

    # 모든 토마토가 익었는지 확인
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if box[i][j][k] == 0:
                    return -1  # 익지 않은 토마토가 남아있는 경우

    return days -1

M, N, H = map(int, input().split())
box = []
for _ in range(H):
    tomatoes = []
    for _ in range(N):
        tomatoes.append(list(map(int, input().split())))
    box.append(tomatoes)
print(tomato_ripening(box,M,N,H))



# ver_2.0
# 큐를 돌린 후 가장 높은 숫자를 출력하는 법
# 특정 위치에 토마토가 언제 익는지 확인하기 좋음
import sys
from collections import deque
m,n,h = map(int,input().split()) # mn크기, h상자수
graph = []
queue = deque([])
 
for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int,sys.stdin.readline().split())))
        for k in range(m):
            if tmp[j][k]==1:
                queue.append([i,j,k])
    graph.append(tmp)
    
dx = [-1,1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
while(queue):
    x,y,z = queue.popleft()
    
    for i in range(6):
        a = x+dx[i]
        b = y+dy[i]
        c = z+dz[i]
        if 0<=a<h and 0<=b<n and 0<=c<m and graph[a][b][c]==0:
            queue.append([a,b,c])
            graph[a][b][c] = graph[x][y][z]+1
            
day = 0
for i in graph:
    for j in i:
        for k in j:
            if k==0:
                print(-1)
                exit(0)
        day = max(day,max(j))
print(day-1)