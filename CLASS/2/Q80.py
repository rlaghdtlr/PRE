while True:
    S = list(map(int, input().split()))
    if S[0] == 0:
        break
    S.sort()
    if S[0]**2 + S[1]**2 == S[2]**2:
        print('right')
    else:
        print('wrong')
    
while True:
    S = list(map(int, input().split()))
    if S[0] == 0:
        break
    
    a, b, c = sorted(S)
    if a**2 + b**2 == c**2:
        print('right')
    else:
        print('wrong')
