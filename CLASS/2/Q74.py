import sys
input = sys.stdin.readline

N = int(input())
Nlist = set(map(int, input().split()))
M = int(input())
Mlist = list(map(int, input().split()))
for i in Mlist:
    if i in Nlist:
        print(1)
    else:
        print(0)

