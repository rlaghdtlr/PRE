#https://www.acmicpc.net/problem/17219
#문제 118 - 비밀번호 찾기

# ver_1.0
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
website = {}
for _ in range(n):
    address, password = map(str, input().split())
    website[address] = password
for _ in range(m):
    find = input().rstrip()
    print(website[find])

