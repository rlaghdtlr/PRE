T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1

    def dfs(y, x):
        stack = [(y, x)]
        while stack:
            y, x = stack.pop()
            if y < 0 or y >= N or x < 0 or x >= M:
                continue
            if field[y][x] == 0:
                continue
            field[y][x] = 0
            stack.append((y-1, x))
            stack.append((y+1, x))
            stack.append((y, x-1))
            stack.append((y, x+1))

    count = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                dfs(i,j)
                count += 1
    print(count)

