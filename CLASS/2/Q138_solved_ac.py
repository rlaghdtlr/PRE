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
und = round(n*0.15) # 평균값 제외할 범위
for i in range(n):
    x = int(input())
    nlist.append(x)
nlist.sort()
print(round(sum(nlist[und:n-und])/(n-(2*und))))

# ver_2.0
# 정답 4사5입을 구현하는 함수를 새로 구성하여 해결
import sys
input = sys.stdin.readline

def round2(num): # 신규반올림 함수 (5사5입)
    return int(num + 0.5)

n = int(input())
if n == 0:
    print(0)
    exit()
nlist = []
und = round2(n*0.15)
for i in range(n):
    x = int(input())
    nlist.append(x)
nlist.sort()
print(round2(sum(nlist[und:n-und])/(n-(2*und))))
