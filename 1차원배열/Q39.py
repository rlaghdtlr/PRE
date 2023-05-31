import sys
input = sys.stdin.readline

n = []

for _ in range(10):
    X = int(input())%42
    n.append(X)

n = set(n)
print(len(n))

