a = int(input())
b = int(input())
c = int(input())
C = [0]*10
S = list(str(a*b*c))
for i in S:
    C[int(i)] += 1
print(*C, sep='\n')

a = int(input())
b = int(input())
c = int(input())

S = str(a*b*c)
for i in range(0, 10):
    print(S.count(str(i)))

    