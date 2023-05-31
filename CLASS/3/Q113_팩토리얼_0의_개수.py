#https://www.acmicpc.net/problem/1676
#문제 113번 - 팩토리얼 0의 개수

# ver_1.0
import sys
input = sys.stdin.readline

def factorial(n):
    memo = {}  # 중간 계산 결과를 저장할 딕셔너리

    def factorial_re(n):
        if n == 0 or n == 1:
            return 1
        if n in memo:
            return memo[n]
        else:
            memo[n] = n * factorial_re(n - 1)
            return memo[n]

    return factorial_re(n)

n = int(input())
count = 0
for i in str(factorial(n))[::-1]:
    if count == 0:
        if i == '0':
            count += 1
    else:
        if i == '0':
            count += 1
        else:
            break
print(count)

# ver_2.0
# 1.0버전의 코드 간소화
import sys
input = sys.stdin.readline

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

count = 0
for i in str(factorial(int(input())))[::-1]:
    if i == '0':
        count += 1
    else:
        break
print(count)

# ver_3.0
# 새로운 로직
import sys
input = sys.stdin.readline

n = int(input().strip())
count = 0

while n > 0:
    count += n // 5
    n //= 5

print(count)

