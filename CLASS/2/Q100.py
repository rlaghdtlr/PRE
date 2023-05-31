n = int(input())
i = 5
j = 3
cnt = n//i
while True:
    t = n
    t -= cnt*i
    if t%j ==0:
        cnt += t//j
        break
    else:
        cnt -=1
    if cnt < 0:
        cnt = -1
        break
print(cnt)

