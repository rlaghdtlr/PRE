#https://www.acmicpc.net/problem/2606
#문제 121 - 바이러스

# ver_1.0
from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    count = -1
    while queue:
        node = queue.popleft()
        count += 1
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    print(count)

n = int(input())
m = int(input())
mgraph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    mgraph[a].append(b)
    mgraph[b].append(a)
bfs(mgraph,1)

# ver_2.0
# 로직간소화
n = int(input())
m = int(input())
visited = [0]*(n+1)
mgraph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    mgraph[a].append(b)
    mgraph[b].append(a)
visited = []
stack = [1]
while stack:
    node = stack.pop()
    if node not in visited:
        visited.append(node)
        stack += mgraph[node]
print(len(visited)-1)
