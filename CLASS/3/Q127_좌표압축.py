#https://www.acmicpc.net/problem/18870
#문제 127 - 좌표압축

# ver_1.0
# 시간초과 오류
import sys
input = sys.stdin.readline

n = int(input())
nlist = list(map(int, input().split()))

nset = set()
nset.update(nlist)
sorted_list = sorted(nset)

for i in range(n):
    print(sorted_list.index(nlist[i]), end=' ')

# ver_2.0
# 딕셔너리를 사용하여 숫자의 인덱스 저장
import sys
input = sys.stdin.readline

n = int(input())
nlist = list(map(int, input().split()))

index_dict = {}
for i, num in enumerate(sorted(set(nlist))):
    index_dict[num] = i

for num in nlist:
    print(index_dict[num], end=' ')
