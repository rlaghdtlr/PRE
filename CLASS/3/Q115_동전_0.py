#https://www.acmicpc.net/problem/11047
#문제 115 - 동전 0

# ver_1.0
import sys
input = sys.stdin.readline

def counting(arr, money):
    i = 0
    count = 0
    while money>0:
        if money - arr[i] >= 0:
            money -= arr[i]
            count += 1
            if money == 0:
                break
            continue
        else:
            i += 1
    return count

n, k = map(int, input().split())
nlist = [int(input().rstrip()) for _ in range(n)]
print(counting(nlist[::-1], k))

# ver_2.0
# 코드 다듬기
import sys
input = sys.stdin.readline

def counting(arr, money):
    count = 0
    for i in arr[::-1]:
        count += money//i
        money = money%i
    return count

n, k = map(int, input().split()) 
nlist = [int(input().rstrip()) for _ in range(n)]
print(counting(nlist, k))