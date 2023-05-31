import sys
input = sys.stdin.readline

subject = int(input())
score = list(map(int, input().split()))
print(sum(score)/subject/max(score)*100)

# import sys
# input = sys.stdin.readline

# subject = int(input())
# score = list(map(int, input().split()))
# sum = 0

# for i in score:
#     sum = sum + i/max(score)*100
# print(sum/subject)