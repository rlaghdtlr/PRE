import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    nlist = deque(map(int, input().split()))
    maxnum = max(nlist)
    count = 0
    while True:
        if maxnum == nlist[0]:
            nlist.popleft()
            count += 1
            if m == 0:
                break
            maxnum = max(nlist)
        else:
            nlist.rotate(-1)
        m += -1 if m > 0 else len(nlist) - 1
    print(count)


import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    nlist = list(map(int, input().split()))
    ready = deque([[i,nlist[i]] for i in range(n)])
    copy = ready[m]
    while ready[0][1] != max(x[1] for x in ready):
        ready.rotate(-1)
    print(ready.index(copy)+1)

import sys
input = sys.stdin.readline
from collections import deque

def order(m, docs):
    queue = deque([(i, d) for i, d in enumerate(docs)])
    order = 0
    while queue:
        p = queue.popleft()
        pi, pd = p[0], p[1]
        if any(pd < i[1] for i in queue):
            queue.append(p)
        else:
            order += 1
            if pi == m:
                return order

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    docs = list(map(int, input().split()))
    print(order(m, docs))


import sys    
for _ in range(int(input())):
    N, target = map(int, sys.stdin.readline().split())
    printer = list(map(int, sys.stdin.readline().split()))
    max_ = max(printer)
    cnt = 0 
    while True:
        if max_ == printer[0]:
            printer.pop(0)
            cnt +=1
            if target == 0: break
            max_ = max(printer)
        else:
            printer.append(printer.pop(0))
        target += -1 if target > 0 else len(printer) - 1
    print(cnt)