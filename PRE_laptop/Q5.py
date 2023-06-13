import sys
import heapq
#heapq 모듈을 사용하여 최소 힙을 구현하였음

#처음 값
num_N = int(sys.stdin.readline())

Y = []
Z = []
min_v = float('inf')

#처음 값 입력받은 만큼 숫자를 입력받는다
for i in range(0,num_N) :
    num_X = int(sys.stdin.readline())
    #Y리스트에 입력받은 값을 넣는다
    #0이 아닐경우
    if num_X != 0:
        heapq.heappush(Y,num_X)
    #0일 경우
    else:
        #Y리스트가 비어있는 경우 0을 Z리스트에 삽입
        if not Y:
            Z.append(0)
        #Y리스트가 비어있지 않는 경우 최소힙을 Z리스트에 넣는다
        else:
            Z.append(heapq.heappop(Y))
#Z리스트 출력
print(*Z, sep='\n')