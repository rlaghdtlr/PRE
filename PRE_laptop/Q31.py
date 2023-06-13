import sys

while (True):
    try:
        num_A, num_B = map(int, sys.stdin.readline().split())
        print(num_A+num_B)
    except:
        break
