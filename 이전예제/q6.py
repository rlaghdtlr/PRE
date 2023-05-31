import sys
import numpy as np

num_N = int(sys.stdin.readline())
# num1, num2 = map(int, input().split())

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
root = Node(1)

