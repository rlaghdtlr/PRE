# https://www.acmicpc.net/problem/18110
# 문제 138 - solved.ac

# ver_1.0
# 틀림 파이썬에서의 round 반올림 함수의 올림방법(5사5입)이 문제에서 요구하는 올림방법(4사5입)과 다름으로 인하여 생기는 오류
import sys
input = sys.stdin.readline

n = int(input())
if n == 0:
    print(0)
    exit()
nlist = []
avg_n = int(n * 0.15 + 0.5)  # 올림 연산
for i in range(n):
    x = int(input())
    nlist.append(x)
nlist.sort()
print(round(sum(nlist[avg_n:n-avg_n])/(n-(2*avg_n))))

# ver_2.0
# 정답 4사5입을 구현하는 함수를 새로 구성하여 해결
import sys
input = sys.stdin.readline

def round2(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)

n = int(input())
if n == 0:
    print(0)
    exit()
nlist = []
und = int(n * 0.15 + 0.5)  # 올림 연산
for i in range(n):
    x = int(input())
    nlist.append(x)
nlist.sort()
print(round2(sum(nlist[und:n-und])/(n-(2*und))))
