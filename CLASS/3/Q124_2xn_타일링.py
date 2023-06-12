#https://www.acmicpc.net/problem/11726
#문제 124 - 2xn 타일링

# ver_1.0
# 동적계획법 사용
n = int(input())
nlist = [0]*(n+1)
nlist[0] = 1
nlist[1] = 1
if n > 1:
    for i in range (2, n+1):
        nlist[i] = (nlist[i-1] + nlist[i-2])%10007
print(nlist[n])

# ver_2.0
# 라이브러리 함수 사용
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)%10007

n = int(input())
print(fibonacci(n))

# ver_3.0
# 1.0버전의 코드 간결화
n=int(input())
nlist=[1,1]+[0]*n
for i in range(2,n+1):
    nlist[i]=(nlist[i-1]+nlist[i-2])%10007
print(nlist[n])