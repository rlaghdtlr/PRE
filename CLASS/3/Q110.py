import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
Mlist = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int,input().split())
    Mlist[a-1].append(b-1)
    Mlist[b-1].append(a-1)

print(Mlist)

def bfs(start):
    visited = [False]*N
    counter = [0]*N
    visited[start] = True
    q = deque([start])
    print(q)
    while q:
        current = q.popleft()
        print(current)
        for i in Mlist[current]:
            if not visited[i]:
                visited[i] = True
                counter[i] = counter[current]+1
                q.append(i)
    return sum(counter)

print(min(range(N), key=lambda i: bfs(i))+1)

