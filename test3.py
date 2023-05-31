# N, M = map(int, input().split())
# board = [input() for _ in range(N)]

# target = ['BWBWBWBW', 'WBWBWBWB'] * 4

# ans = 32
# for i in range(N - 7):
# 	for j in range(M - 7):
# 		cnt = 0
# 		for k in range(8):
# 			for x in zip(target[k], board[i + k][j:j + 8]):
# 				cnt += (x[0] != x[1])
# 		ans = min(ans, cnt, 64 - cnt)
# print(ans)

d = { 'B': 'W', 'W': 'B' }
#변환기준

#체스판크기기준

N, M = map(int, input().split())
board = [[*input()] for _ in range(N)]
#입력부

for i in range(N):
	for j in range(M):
		if not (i + j) % 2:
			board[i][j] = d[board[i][j]]
#변환부

ans = 32
for i in range(N-7):
	for j in range(M-7):
		cnt = sum(board[i + k][j:j+8].count('W') for k in range(8))
		ans = min(ans, cnt, 64 - cnt)
#비교부
print(ans)


# print(ans)

