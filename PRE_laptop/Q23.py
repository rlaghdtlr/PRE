import sys

num_N = int(sys.stdin.readline())
j = 0
for i in range(1,num_N+1):
    j = i+j
print(j)

