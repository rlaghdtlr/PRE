#https://www.acmicpc.net/problem/2579
#문제 120 - 계단 오르기

# ver_1.0
import sys
input = sys.stdin.readline

def maxnum(nlist, n):
    if n == 1:
        return nlist[0]
    elif n == 2:
        return (nlist[0] + nlist[1])
    
    dp = [0] * n
    dp[0] = nlist[0]
    dp[1] = nlist[0] + nlist[1]
    
    for i in range(2, n):
        dp[i] = max(dp[i-2] + nlist[i], dp[i-3] + nlist[i-1] + nlist[i])
    return dp[-1]

n = int(input())
nlist = [int(input()) for _ in range(n)]

result = maxnum(nlist, n)
print(result)

# ver_2.0
# 코드 간소화
n = int(input())
nlist = [int(input()) for _ in range(n)]
if n == 1 or n == 2:
    print(sum(nlist))
else:
    dp = [0] * n
    dp[0] = nlist[0]
    dp[1] = nlist[0] + nlist[1]

    for i in range(2, n):
        dp[i] = max(dp[i-2], dp[i-3] + nlist[i-1]) + nlist[i]
    print(dp[-1])