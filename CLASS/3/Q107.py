n,r,c = map(int,input().split())
size = 2**n

_sum = '0b'
while size >= 2:
    if size > r >= size//2 :
        r -= size//2
        if size > c >= size//2:
            c -= size//2
            _sum += '11'
        else:
            _sum += '10'
    else:
        if size > c >= size//2:
            c -= size//2
            _sum += '01'
        else:
            _sum += '00'
    size //= 2
print(int(_sum,2))


def zpath(i, j, N):
    if N == 0:
        return 0
    else:
        n_block=2**(2*(N-1))
        return (i//2**(N-1) + 2*(j//2**(N-1)))*n_block + zpath(i%2**(N-1), j%2**(N-1), N-1)
N, c, r=map(int, input().split())
print(zpath(r, c, N))
