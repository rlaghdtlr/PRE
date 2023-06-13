import sys

num_N = int(sys.stdin.readline())

for i in range(num_N):
    num_A, num_B = map(int, sys.stdin.readline().split())
    print (num_A+num_B)

