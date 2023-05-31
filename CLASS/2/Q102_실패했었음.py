import sys
input = sys.stdin.readline
from collections import Counter
n = int(input())
nlist = []
for _ in range(n):
    nlist.append(int(input()))

print(round(sum(nlist)/n))
nlist.sort()
print(nlist[n//2])

cnt_nlist = Counter(nlist).most_common()
if len(cnt_nlist) > 1 and cnt_nlist[0][1]==cnt_nlist[1][1]:
    print(cnt_nlist[1][0])
# 최빈값 두개 이상일경우 출력 (두번째 작은 값)
else:
    print(cnt_nlist[0][0])
print(max(nlist)-min(nlist))


