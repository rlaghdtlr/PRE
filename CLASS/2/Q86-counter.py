import sys
input = sys.stdin.readline

n = int(input())
ncards = list(map(int, input().split()))
m = int(input())
mcards = list(map(int, input().split()))

ncards_count = {}
for card in ncards:
    ncards_count[card] = ncards_count.get(card, 0) + 1

for card in mcards:
    print(ncards_count.get(card, 0), end=' ')

import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
ncards = list(map(int, input().split()))
m = int(input())
mcards = list(map(int, input().split()))

ncards_count = Counter(ncards)

for card in mcards:
    print(ncards_count[card], end=' ')