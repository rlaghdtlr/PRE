import sys
input = sys.stdin.readline

n = int(input())
plist = [int(input()) for _ in range(n)]
stack = []
result = []
num = 1

for i in plist:
    while num <= i:
        stack.append(num)
        result.append('+')
        num += 1

    if stack[-1] == i:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        exit(0)

print(*result, sep='\n')

