import sys
input = sys.stdin.readline

n = int(input())
spot = []
for _ in range(n):
    spot.append(list(map(int, input().split())))
spot.sort(key = lambda x: (x[1], x[0]))
for i in spot:
    print(*i)

    