# +,- 수식과 최대 5자리수의 숫자가 입력됨
# 수식결과가 제일 작은 값이 나오게 해야함
# - 뒤에 오는 숫자가 제일 커지게 만드는게 중요
# - 뒤에오는 숫자들은 다음 -가 오기 전까지 괄호로 묶어 우선계산되도록 함
import re
s = input()
s = re.sub(r'\b0+(\d+)', r'\1', s)
s = re.sub(r'-0+', '-', s)
s = re.sub(r'\+0+', '+', s)
s = list(s)

minus = 0
for i in range(len(s)):
    if s[i] == '-':
        if minus == 1:
            s[i] = ')-('
        elif minus == 0:
            s[i] = '-('
            minus = 1
if minus == 1:
    s.append(")")
print(eval(''.join(s)))


import sys
input = sys.stdin.readline

arr = input().rstrip().split('-')
sum_ = sum(list(map(int, arr[0].split('+'))))
for i in arr[1:]:
    sum_ -= sum(list(map(int, i.split('+'))))
print(sum_)
