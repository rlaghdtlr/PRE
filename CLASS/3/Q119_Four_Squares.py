#https://www.acmicpc.net/problem/17626
#문제 119 - Four Squares

# ver_1.0
# 정석계산
import sys
input = sys.stdin.readline

def four_squares(n):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, int(n ** 0.5) + 1):
        sq = i * i
        for j in range(sq, n + 1):
            dp[j] = min(dp[j], dp[j - sq] + 1)
    return dp[n]
n = int(input())
print(four_squares(n))

# ver_2.0
# 로직개선
n = int(input())
m = int(n**.5)
sq1 = [i*i for i in range(1,m+1)]
sq2 = []
for i in range(0,m):
    for j in range(0,i+1):
        sq2.append(sq1[i] + sq1[j])
if n in sq1:
    print(1)
elif n in sq2:
    print(2)
else:
    for s in sq1:
        if n - s in sq2:
            print(3)
            break
    else:
        print(4)