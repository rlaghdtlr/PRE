import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    t = input().rstrip()
    count = 0
    for i in t:
        if i == '(':
            count += 1
        elif count >= 1 and i == ')':
            count -= 1
        else:
            print('NO')
            break
    else:
        if count == 0:
            print('YES')
        else:
            print('NO')

