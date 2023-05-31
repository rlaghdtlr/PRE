import sys
input = sys.stdin.readline

big = []
ranking = []
n = int(input())
for _ in range(n):
    big.append(list(map(int, input().split())))
for i in big:
    rank = 1
    for j in big:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    ranking.append(rank)
print(*ranking, end=' ')


import sys
input = sys.stdin.readline

class Person:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
        self.rank = 1

n = int(input())
big = []
for i in range(n):
    x, y = map(int, input().split())
    big.append(Person(x, y))

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if big[i].weight < big[j].weight and big[i].height < big[j].height:
            big[i].rank += 1

for i in big:
    print(i.rank, end=' ')