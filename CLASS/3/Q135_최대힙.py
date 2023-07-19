# https://www.acmicpc.net/problem/11279
# 문제 135 - 최대 힙

# ver_1.0
import sys
input = sys.stdin.readline
import heapq

heap = []
N = int(input())
for _ in range(N):
    x = int(input())
    if x > 0:
        heapq.heappush(heap, -x)
    elif x == 0:
        if heap:
            maxnum = heapq.heappop(heap)
            print(-maxnum)
        else:
            print(0)

# ver_2.0 코드 간소화
import heapq
import sys
input = sys.stdin.readline

heap = []
N = int(input())
for _ in range(N):
    x = int(input())
    if x > 0:
        heapq.heappush(heap, -x)
    elif x == 0:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)