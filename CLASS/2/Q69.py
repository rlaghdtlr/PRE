import sys
n = int(input())
S = [sys.stdin.readline().rstrip() for _ in range(n)]
S = sorted(list(set(S)), key=lambda x: (len(x), x))
print(*S, sep='\n')

