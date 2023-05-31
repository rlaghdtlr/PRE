import sys

list_L = []

for i in range (9):
    list_L.append(int(sys.stdin.readline()))

print(max(list_L))
print(list_L.index(max(list_L))+1)

