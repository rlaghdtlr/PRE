n, m = map(int, input().split())
LIST = [i for i in range(1,n+1)]

for _ in range(m):
    i, j, k = map(int, input().split())
    LIST = *LIST[:i-1],*LIST[k-1:j],*LIST[i-1:k-1],*LIST[j:]
print(*LIST)

