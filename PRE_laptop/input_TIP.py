# 1. 한 개의 정수를 입력받을 때

import sys
a = int(sys.stdin.readline()) # input()을 이용해도 무방함.



# 2. 정해진 개수의 정수를 한 줄에 입력받을 때

# map()은 반복 가능한 객체 (예 - 리스트) 에 대해 각각의 요소들을 지정된 함수로 처리해주는 함수임.
a, b, c = map(int, sys.stdin.readline().split())

# 3. 임의의 개수의 정수를 한 줄에 입력받아 리스트에 저장할 때
data = list(map(int, sys.stdin.readline().split()))

# 4. 임의의 개수의 정수를 n줄 입력받아 2차원 리스트에 저장할 때

n = int(sys.stdin.readline())
# strip()는 문자열 맨 앞과 맨 끝의 공백문자를 제거함. (한 줄씩 끊어냄.)
data = [sys.stdin.readline().strip() for i in range(n)]

