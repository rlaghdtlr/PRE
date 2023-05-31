

#백준 문제 풀기
#첫째 줄에 정수 n(1 ≤ n ≤ 100,000)이 주어지고 
#둘째 줄에는 n개의 정수로 이루어진 수열이 주어진다.
#수는 -1,000보다 크거나 같고, 1,000보다 작거나 같은 정수이다.

import random


rand_num = random.randint(1,10)

#n = 수열의 개수
# numlist = [random.randint(-1000,1000) for value in range(0, rand_num)]
numbers = [random.randint(-20,20) for value in range(0, rand_num)]
num1 = 0
num2 = 0
#num1 리스트 덧셈 저장
#num2 리스트 뺄셈 저장
#num3 리스트 비교값 저장

print("입력부분입니다")
print (rand_num)
print (numbers)
if numbers[0] < 0 :
    num1 = numbers[0]

for number in numbers:
    # print(number)
    # 양수인 경우
    if number>=0 :
        if (num1 < 0) :
            num1 = 0
        num1 = num1 + number
    # 음수인경우 더해져도 1 이상인 경우
    elif num1+number>0 :
        num2 = num1
    # 음수인경우 더해졌을때 0 이하인 경우 (필요없음)
    else :
        num2 = num1
        num1 = 0
print("출력부분입니다")
print("num1: ",num1)
print("num2: ",num2)
if num1>=num2 : print(num1)
else : print(num2)


# for(i=0; i =< n ; i++) {
# if (numlist[i]>=0) {
#     num1 += numlist[i];
# } else if (num1-numlist[i]>0) {
#     num2 = num1;
#     num1 += numlist[i];
# } else 
# num2 = num1;
# num1 = 0;
# }
# if (num1 >= num2) { print(num1);}
# else print(num2);
# #num1과 num2 크기 비교해서 큰 수 출력