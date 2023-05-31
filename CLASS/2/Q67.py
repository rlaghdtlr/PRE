#입력부
n, m = map(int, input().split())
board = [[*input()] for _ in range(n)]
#변환부
check = {'W':'B','B':'W'}

for i in range(n):
    for j in range(m):
        if not (i+j)%2:
            board[i][j] = check[board[i][j]]

#비교부
df = 32
for i in range(n-7):
    for j in range(m-7):
        count = sum(board[i+k][j:j+8].count('W') for k in range(8))
        df = min(df, count, 64-count)

#출력
print(df)



