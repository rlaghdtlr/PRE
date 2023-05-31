import sys

num1 = int(sys.stdin.readline())
if num1 < 100:
    count = num1
elif num1 == 1000:
    count = 144
else:
    count = 99
    for i in range(100, num1+1):
        li = [*str(i)]
        # print(li)
        if (int(li[0]) - int(li[1]) == int(li[1]) - int(li[2])):
            count = count+1
            # print("count up!")
print(count)