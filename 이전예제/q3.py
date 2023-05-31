import sys

num1 = int(sys.stdin.readline())
y = [0]*100000

if num1 != 1:
    for i in range(1, num1+1):
        num2 = int(sys.stdin.readline())
        if num2 != 0:
            y.append(num2)
        else:
            y.pop()
else:
    y[0] = int(sys.stdin.readline())

print(sum(map(int, y)))

# 정수 k입력받고 y[]행렬의 길이가 k인 정수행렬 
# y[n]은 0~1,000,000값범위 y[n]에 정수가0이 들어가면 
# 직전에 입력된 행렬 (y[n-1]의 값을 초기화 하고
# y[n-1]값부터 다시 입력받아 넣음 최종적으로 y[]값 합산해서 출력