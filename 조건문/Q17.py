import sys

num_X = int(sys.stdin.readline())
num_Y = int(sys.stdin.readline())

if num_X > 0 :
    if num_Y > 0 :
        print(1)
    else :
        print(4)
else :
    if num_Y > 0 :
        print(2)
    else :
        print(3)
