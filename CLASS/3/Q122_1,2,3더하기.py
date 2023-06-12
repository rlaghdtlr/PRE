#https://www.acmicpc.net/problem/9095
#문제122 - 1,2,3더하기

# ver_1.0
# 동적계획법 사용
import sys
input = sys.stdin.readline

def count_sum_way(n):
    # 0부터 n까지의 경우의 수를 저장할 배열 초기화
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        if i >= 1:
            dp[i] += dp[i - 1]
        if i >= 2:
            dp[i] += dp[i - 2]
        if i >= 3:
            dp[i] += dp[i - 3]

    return dp[n]

T = int(input())
for _ in range(T):
    n = int(input())
    print(count_sum_way(n))