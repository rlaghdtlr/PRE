C = int(input())
for i in range(C):
    N = list(map(int, input().split()))
    avg = sum(N[1:])/N[0]
    good = 0
    for j in N[1:]:
        if j >avg :
            good += 1
    print("{:.3f}%".format(good/N[0]*100))

