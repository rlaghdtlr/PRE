import sys
input = sys.stdin.readline

n, m = map(int, input().split())
list_L = [i for i in range(1, n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    list_L[i-1], list_L[j-1] = list_L[j-1], list_L[i-1]
print(*list_L)

# import sys

# num_N, num_M = map(int, sys.stdin.readline().split())
# list_L = [i for i in range(1,num_N+1)]

# for i in range (num_M):
#     num_i, num_j = map(int, sys.stdin.readline().split())
#     num_A = list_L[num_i-1]
#     list_L[num_i-1] = list_L[num_j-1]
#     list_L[num_j-1] = num_A
# print(*list_L)