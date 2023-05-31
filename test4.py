N = int(input())
M = int(input())
if M != 0:
    button = set(range(10)) - set(map(int, input().split()))
else:
    button = set(range(10))

count = abs(N-100)
for i in range(1000000):
    for j in str(i):
        if int(j) not in button:
            break
    else:
        count = min(count, len(str(i)) + abs(i-N))

print(count)

