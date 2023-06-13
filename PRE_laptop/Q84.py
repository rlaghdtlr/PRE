import sys
input = sys.stdin.readline

n = int(input())
people = [input().split() for _ in range(n)]
sorted_list = sorted(people, key=lambda x:int(x[0]))
for i in sorted_list:
    print(*i)

    