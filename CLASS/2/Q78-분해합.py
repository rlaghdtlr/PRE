# n = int(input())

# for i in range(1, n+1):
#     if n == i + sum(map(int, str(i))):
#         print(i)
#         exit(0)
# print(0)

n = int(input())
start = max(1, n - 9 * len(str(n)))
for i in range(start, n+1):
    if n == i + sum(map(int, str(i))):
        print(i)
        exit(0)
print(0)

