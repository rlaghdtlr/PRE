A, B = map(str, input().split())
A = int(A[::-1])
B = int(B[::-1])
if A>B:
    print(A)
else:
    print(B)

A, B = input().split()

A = A[::-1]
B = B[::-1]

print(max(A, B))