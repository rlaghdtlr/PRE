# https://www.acmicpc.net/problem/1697
# 문제 129 - 숨바꼭질

# ver_1.0
from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

def bfs(n, k):
    queue = deque([(n, 0)]) # 시작 위치와 시간을 큐에 넣음
    visited = [False] * 100001 # 방문 여부를 저장할 리스트
    visited[n] = True

    while queue:
        pos, time = queue.popleft()

        if pos == k:  # 동생을 찾은 경우
            return time

        # 걷는 경우
        if pos - 1 >= 0 and not visited[pos - 1]:
            queue.append((pos - 1, time + 1))
            visited[pos - 1] = True

        if pos + 1 <= 100000 and not visited[pos + 1]:
            queue.append((pos + 1, time + 1))
            visited[pos + 1] = True

        # 순간이동하는 경우
        if pos * 2 <= 100000 and not visited[pos * 2]:
            queue.append((pos * 2, time + 1))
            visited[pos * 2] = True

    return -1  # 동생을 찾지 못한 경우

result = bfs(n, k)
print(result)

# ver_2.0
# 코드 간결화
from collections import deque

def bfs(n, k):
  q = deque()
  q.append(n)
  while q:
    x = q.popleft()
    if x == k:
      print(dp[x])
      break
    for nx in (x-1, x+1, x*2):
      if 0 <= nx <= 100000 and not dp[nx]:
        dp[nx] = dp[x] + 1
        q.append(nx)

N, K = map(int, input().split())
dp = [0] * 100001

bfs(N, K)