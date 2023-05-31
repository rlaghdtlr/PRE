T = int(input())
for _ in range(T):
    R, S = map(str, input().split())
    R = int(R)
    for i in S:
        for j in range(R):
            print(i, end='')
    print()

# T = int(input())
# for _ in range(T):
#     R, S = map(str, input().split())
#     for i in S:
#         print(i*int(R), end='')
#     print()

