import sys

num_T = int(sys.stdin.readline())
for i in range(num_T) :
    num_A, num_B = map(int, sys.stdin.readline().split())
    print(num_A+num_B)

