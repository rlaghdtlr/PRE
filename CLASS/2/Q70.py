while True:
    S = input()
    if S == '0':
        break
    if S == S[::-1]:
        print('yes')
    else:
        print('no')

