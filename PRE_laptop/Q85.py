import sys
input = sys.stdin.readline

n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))
numbers.sort()
print(*numbers,sep='\n')



import sys
input = sys.stdin.readline

n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input().rstrip()))

numbers.sort()
print('\n'.join(map(str, numbers)))
