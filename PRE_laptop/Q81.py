import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    h, w, n = map(int, input().split())
    room = 1
    if n%h == 0:
        room += (n//h)-1 + h*100
    else:
        room += (n//h) + n%h*100
    print(room)

import sys
T = int(sys.stdin.readline())
for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().rstrip().split())
    result1 = str((N-1) % H+1)
    result2 = (2 - len(str((N-1)//H+1)))*"0" + str((N-1)//H+1)
    print(result1 + result2)
