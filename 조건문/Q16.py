import sys

num_A = int(sys.stdin.readline())

if num_A % 4 == 0 :
    if num_A % 400 == 0 or num_A % 100 != 0 :
        print(1)
    else :
        print(0)
else :
    print(0)