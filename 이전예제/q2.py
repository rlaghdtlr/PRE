num1, num2 = map(int, input().split())

y = [0]*10000
j = 0

for i in range(1, num1+1):
    if num1%i == 0:
        y[j] = i
        j = j+1
print(y[num2-1])

