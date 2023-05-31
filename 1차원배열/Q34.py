import sys

num_N, num_X = map(int, sys.stdin.readline().split())
list_L = list(map(int, sys.stdin.readline().split()))

for i in list_L:
    if i < num_X:
        print(i, end=' ')

