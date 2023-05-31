N = int(input())

for _ in range(N):
    S = input()
    score = 0
    stack = 0
    for i in S:
        if i == 'O':
            stack += 1
        else :
            stack = 0
        score += stack
    print(score)

