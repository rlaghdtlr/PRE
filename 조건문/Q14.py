import sys

num_A, num_B = map(int, sys.stdin.readline().split())

if num_A > num_B :
    print(">")
elif num_A == num_B :
    print("==")
else :
    print("<")

