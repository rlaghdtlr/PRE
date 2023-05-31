N = int(input())
Nlist = list(map(int, input().split()))
check = 0
for i in Nlist:
    if i < 2:
        continue
    for j in range(2, int(i**0.5)+1):
        if i%j == 0:
            break
    else:
        check += 1
print(check)

