import sys
from collections import deque
input = sys.stdin.readline

def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack += sorted(graph[node], reverse=True)
    return visited

def bfs(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue += sorted(graph[node])
    return visited

n,m,v = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
print(*dfs(graph,v),sep=' ')
print(*bfs(graph,v),sep=' ')

