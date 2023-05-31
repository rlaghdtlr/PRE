import sys

num_A = int(sys.stdin.readline())

if num_A >= 90 :
    print("A")
elif num_A >= 80 :
    print("B")
elif num_A >= 70 :
    print("C")
elif num_A >= 60 :
    print("D")
else :
    print("F")
