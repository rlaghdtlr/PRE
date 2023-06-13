N = int(input())

for i in range(N-1, 0, -1):
    print(' '*i+'*'*(2*(N-i)-1))
for j in range(N):
    print(' '*j+'*'*(2*(N-j)-1))

