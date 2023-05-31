from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
queue = deque()
for _ in range(n):
    order = input().split()
    if 'push_front' in order:
        queue.appendleft(int(order[1]))
    elif 'push_back' in order:
        queue.append(int(order[1]))
    elif 'pop_front' in order:
        if not queue:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()
    elif 'pop_back' in order:
        if not queue:
            print(-1)
        else:
            print(queue[-1])
            queue.pop()
    elif 'size' in order:
        print(len(queue))
    elif 'empty' in order:
        if not queue:
            print(1)
        else:
            print(0)
    elif 'front' in order:
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif 'back' in order:
        if not queue:
            print(-1)
        else:
            print(queue[-1])


