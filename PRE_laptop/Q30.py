import sys

num_N = int(sys.stdin.readline())

for i in range (1,num_N+1):
    for j in range (num_N-i):
        print(' ', end='')
    for j in range (i):
        print('*', end='')
    print()

