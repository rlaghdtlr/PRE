import sys

num_T = int(sys.stdin.readline())
num_C = int(sys.stdin.readline())
num_S = 0

for i in range(num_C):
    num_A, num_B = map(int, sys.stdin.readline().split())
    num_S = num_S + (num_A*num_B)

if (num_T == num_S) :
    print('Yes')
else :
    print('No')

