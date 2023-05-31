N = list(map(int, input().split()))
A = [i for i in range(1, 9)]
B = [i for i in range(8, 0, -1)]
if N == A:
    print('ascending')
elif N == B:
    print('descending')
else:
    print('mixed')

N = list(map(int, input().split()))
if N == sorted(N):
    print('ascending')
elif N == sorted(N, reverse=True):
    print('descending')
else:
    print('mixed')

    