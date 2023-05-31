#https://www.acmicpc.net/problem/11723
#문제 117 - 집합

# ver_1.0
# 오답 - 시간초과, 메모리초과
import sys
input = sys.stdin.readline

m = int(input())
s = set()
for i in range(m):
    mlist = list(map(str, input().split()))
    if mlist[0] == 'add':
        s.add(mlist[1])
    elif mlist[0] == 'remove':
        s.discard(mlist[1])
    elif mlist[0] == 'check':
        print(int(mlist[1] in s))
    elif mlist[0] == 'toggle':
        if mlist[1] in s:
            s.discard(mlist[1])
        else:
            s.add(mlist[1])
    elif mlist[0] == 'all':
        s = set()
        for i in range(1,21):
            s.add(str(i))
    elif mlist[0] == 'empty':
        s = set()

# ver_2.0
# 위의 코드 개선
import sys
input = sys.stdin.readline

m = int(input())
s = set()
for _ in range(m):
    mlist = input().strip().split()
    if len(mlist) == 1:
        if mlist[0] == "all":
            s = set([i for i in range(1, 21)])
        else:
            s = set()
    else:
        f, n = mlist[0], mlist[1]
        n = int(n)
        if f == "add":
            s.add(n)
        elif f == "remove":
            s.discard(n)
        elif f == "check":
            print(1 if n in s else 0)
        elif f == "toggle":
            if n in s:
                s.discard(n)
            else:
                s.add(n)

