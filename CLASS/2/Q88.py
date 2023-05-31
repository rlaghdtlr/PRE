import sys
input = sys.stdin.readline
n = int(input())
nlist = []
for _ in range(n):
    order = input().split()
    if 'push' in order:
        nlist.append(int(order[1]))
    elif 'top' in order:
        if not nlist:
            print(-1)
        else:
            print(nlist[-1])
    elif 'size' in order:
        print(len(nlist))
    elif 'empty' in order:
        if not nlist:
            print(1)
        else:
            print(0)
    elif 'pop' in order:
        if not nlist:
            print(-1)
        else:
            print(nlist[-1])
            nlist.pop()

