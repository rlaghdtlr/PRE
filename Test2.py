N = list(map(int, input().split()))

def ver(list):
    sum = 0
    for i in list:
        sum += i**2
    return sum%10
print(ver(N))

