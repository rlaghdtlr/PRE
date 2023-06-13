#방법 1
import sys

input = sys.stdin.readline
ground = []
n, m, b = map(int,input().split())
for _ in range(n):
    ground += (list(map(int, input().split())))
time = sys.maxsize
idx = 0

# 높이 0~256
for target in range(257):
    max_target, min_target = 0, 0
    for i in ground:
        # 현재 땅이 타겟보다 높으면
        if i >= target:
            max_target += i - target
        # 현재 땅이 타겟보다 낮으면
        else:
            min_target += target - i
        #블록개수가 충분하면
    if max_target + b >= min_target:
        # 최소시간구하기
        if min_target + (max_target * 2) <= time:
            time = min_target + (max_target * 2)
            idx = target
print(time, idx)


#방법2
import sys

n, m, b = map(int, input().split())
g = []
for i in range(n):
    g += list(map(int, input().split()))
sum_g, max_g, min_g = sum(g), max(g), min(g)

#[시간값이 들어가는 리스트]
a = []
#최대높이부터 최소높이까지
for i in range(max_g, min_g-1, -1):
    #모든 땅의 개수 + 가지고 있는 블록의 개수로
    #i높이를 이루는 땅을 만들기에 충분한가
    if sum_g+b >= i*n*m:
        time = 0
        for j in g:
            #땅의 높이를 i로 맞추는 작업
            o = j-i
            #i보다 땅이 낮으면 시간은 1초 소요
            #i보다 땅이 높으면 시간은 2초 소요
            time += abs(o) * (1 + int(o > 0))
        #i일때 시간값을 더함
        a += [time]
    #땅을 못만드는경우 제일큰값을 넣어 최소시간에서 제외
    else: a += [sys.maxsize]

#시간이 최소일때 땅의 높이는 최대높이에서 a인덱스값을 뺀 높이
print(min(a), max_g-a.index(min(a)))

