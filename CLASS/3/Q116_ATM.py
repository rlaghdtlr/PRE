#https://www.acmicpc.net/problem/11399
#문제 116 - ATM

# ver_1.0
import sys
input = sys.stdin.readline

n = int(input())
nlist = list(map(int, input().split()))

nlist.sort()
timelist = []
time = 0
for i in nlist:
    time += i
    timelist.append(time)
print(sum(timelist))

# ver_2.0
# 코드 개선
import sys
input = sys.stdin.readline

n = int(input())  
nlist = list(map(int, input().split()))  

nlist.sort()  
time = 0  
for i in range(1, n+1):
    time += sum(nlist[0:i]) 
print(time)
