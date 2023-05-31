import sys

num_N = list(map(int, sys.stdin.readline().split()))

if num_N[0] == num_N[1] :
    if num_N[1] == num_N[2] :
        num_N[0] = num_N[0]*1000 + 10000
    else :
        num_N[0] = num_N[0]*100 + 1000
elif num_N[1] == num_N[2] :
    num_N[0] = num_N[1]*100 + 1000
elif num_N[0] == num_N[2] :
    num_N[0] = num_N[0]*100 + 1000
else :
    num_N[0] = max(num_N)*100

print(num_N[0])

# a, b, c = map(int, input().split())
# if a == b == c :
#     print(10000+(a)*1000)
# elif a == b :
#     print(1000+(a)*100)
# elif a == c :
#     print(1000+(a)*100)
# elif b == c :
#     print(1000+(b)*100)
# else :
#     print(100 * max(a, b, c))
