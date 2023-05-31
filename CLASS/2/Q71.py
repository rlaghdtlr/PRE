n = int(input())
count = 0
num = 666

while True:
    if '666' in str(num):
        count += 1
    if count == n:
        print(num)
        break
    num += 1

n = int(input())

count = 0
i = 666
while True:
    if '666' in str(i):
        count += 1
        if count == n:
            print(i)
            break
    i += 1

n = int(input())
num = 666
while n>1:
    num += 1
    if '666' in str(num):
        n -= 1
print(num)