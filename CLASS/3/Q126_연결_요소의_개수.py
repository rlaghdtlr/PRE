#https://www.acmicpc.net/problem/11724
#문제 126 - 연결 요소의 개수

# ver_1.0
# 런타임 오류, 이유는 재귀호출이 많이 반복되기 때문
import sys
input = sys.stdin.readline

def dfs(graph, start, visited):
    visited[start] = 1
    
    for node in graph[start]:
        if not visited[node]:
            dfs(graph, node, visited)

n, m = map(int, input().split())
visited = [0] * (n + 1)
mgraph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    mgraph[a].append(b)
    mgraph[b].append(a)

count = 0
for i in range(1, n + 1):
    if not visited[i]:
        dfs(mgraph, i, visited)
        count += 1

print(count)

# ver_2.0
# 코드개선 재귀호출을 없애고 sat형태와 스택을 사용하여 시간복잡도, 메모리 최적화
import sys
input = sys.stdin.readline

def dfs(graph, start, visited):
    stack = [start]
    visited.add(start)
    
    while stack:
        node = stack.pop()
        for n in graph[node]:
            if n not in visited:
                stack.append(n)
                visited.add(n)

n, m = map(int, input().split())
visited = set()
mgraph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    mgraph[a].append(b)
    mgraph[b].append(a)

count = 0
for i in range(1, n + 1):
    if i not in visited:
        dfs(mgraph, i, visited)
        count += 1

print(count)