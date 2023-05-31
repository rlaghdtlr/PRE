import sys
import heapq

num_N = int(sys.stdin.readline())
Y = []
Z = []
min_v = float('inf')
for i in range(0,num_N) :
    num_X = int(sys.stdin.readline())
    if num_X != 0:
        heapq.heappush(Y, num_X)
    else:
        if not Y:
            Z.append(0)
        else:
            Z.append(heapq.heappop(Y))
print(*Z, sep='\n')