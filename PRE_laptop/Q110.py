# import sys
# from collections import Counter
# input = sys.stdin.readline

# N, M = map(int, input().split())
# # Mlist = [list(map(int,input().split())) for _ in range(M)]

# Mlist = []
# for _ in range(M):
#     X,Y = map(int, input().split())
#     if (X,Y) in Mlist or (Y,X) in Mlist:
#         continue  # 이미 입력된 값이면 건너뜁니다.
#     Mlist.append((X,Y))
# # print(Mlist)
# Mlist = [elem for tup in Mlist for elem in tup]
# # print(Mlist)
# counter = Counter(Mlist)
# most_common = counter.most_common(1)
# print(most_common[0][0])


import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
Mlist = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    Mlist[a-1].append(b-1)
    Mlist[b-1].append(a-1)

def bfs(start):
    visited = [False] * N
    counter = [0] * N
    visited[start] = True
    q = deque([start])
    
    while q:
        current = q.popleft()
        for i in Mlist[current]:
            if not visited[i]:
                visited[i] = True
                counter[i] = counter[current] + 1
                q.append(i)
    return sum(counter)

print(min(range(N), key=lambda i: bfs(i))+1)

