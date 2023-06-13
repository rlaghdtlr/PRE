import sys
input = sys.stdin.readline

n = int(input())
nlist = [list(map(int, input().split())) for _ in range(n)]
sorted_list = sorted(nlist, key=lambda x:(x[0], x[1]))
for i in sorted_list:
    print(*i)

    