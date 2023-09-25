# https://www.acmicpc.net/problem/20529
# 문제 142 - 가장 가까운 세 사람의 심리적 거리

# # ver_1.0
# # 시간초과 오답
# import sys
# input = sys.stdin.readline

# def mbti_distance(type1, type2):
#     # 두 MBTI 유형 간의 심리적인 거리를 계산하는 함수
#     distance = 0
#     for i in range(4):  # 네 가지 척도에 대해 반복
#         if type1[i] != type2[i]:
#             distance += 1
#     return distance

# def find_closest_students(mbti_list):
#     min_distance = float('inf')  # 초기 최소 거리를 무한대로 설정
#     n = len(mbti_list)

#     for i in range(n):
#         for j in range(i + 1, n):
#             for k in range(j + 1, n):
#                 # 세 학생 간의 모든 조합을 비교하여 최소 거리 업데이트
#                 distance = (
#                     mbti_distance(mbti_list[i], mbti_list[j]) +
#                     mbti_distance(mbti_list[j], mbti_list[k]) +
#                     mbti_distance(mbti_list[i], mbti_list[k])
#                 )
#                 min_distance = min(min_distance, distance)

#     return min_distance

# # 입력 처리 및 결과 출력
# T = int(input())  # 테스트 케이스 수 입력
# for _ in range(T):
#     N = int(input())  # 학생 수 입력
#     Nlist = list(input().split())  # MBTI 유형 입력
#     min_distance = find_closest_students(Nlist)
#     print(min_distance)


# ver_2.0
# 33명이 입력되면 무조건 답 0
# 여전히 시간초과 오답
# import sys
# input = sys.stdin.readline

# def mbti_distance(type1, type2):
#     # 두 MBTI 유형 간의 심리적인 거리를 계산하는 함수
#     distance = 0
#     for i in range(4):  # 네 가지 척도에 대해 반복
#         if type1[i] != type2[i]:
#             distance += 1
#     return distance

# def find_closest_students(mbti_list):
#     min_distance = float('inf')  # 초기 최소 거리를 무한대로 설정
#     n = len(mbti_list)

#     for i in range(n):
#         for j in range(i + 1, n):
#             for k in range(j + 1, n):
#                 # 세 학생 간의 모든 조합을 비교하여 최소 거리 업데이트
#                 distance = (
#                     mbti_distance(mbti_list[i], mbti_list[j]) +
#                     mbti_distance(mbti_list[j], mbti_list[k]) +
#                     mbti_distance(mbti_list[i], mbti_list[k])
#                 )
#                 min_distance = min(min_distance, distance)
#     return min_distance

# # 입력 처리 및 결과 출력
# T = int(input())  # 테스트 케이스 수 입력
# for _ in range(T):
#     N = int(input())  # 학생 수 입력
#     if N==33:
#         print(0)
#         continue
#     Nlist = input().rstrip().split()  # MBTI 유형 입력
#     min_distance = find_closest_students(Nlist)
#     print(min_distance)



# ver_3.0
# 비둘기집 원리, 브루투포스 알고리즘 사용 == 그냥 노가다 알고리즘
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
	N = int(input())
	Nlist = list(input().split())
	if N>32:
		print(0)
	else:
		ans = 100000
		p = []

		def dfs(start):
			global ans
			if len(p)==3:
				temp = 0
				for i in range(4):
					if(p[0][i]!=p[1][i]):
						temp +=1
					if(p[1][i]!=p[2][i]):
						temp +=1
					if(p[2][i]!=p[0][i]):
						temp +=1
				ans = min(ans,temp)
				return
			for i in range(start,N):
				p.append(Nlist[i])
				dfs(i+1)
				p.pop()
		dfs(0)
		print(ans)

# ver_4.0
# 파이썬 라이브러리 사용
from itertools import combinations
import sys
input = sys.stdin.readline

def mbti_dist(a, b):
	dist = 0
	for i, j in zip(a, b):
		if i != j:
			dist += 1
	return dist

def find_closest_students(mbti_list):
	res = 13    # 세 사람의 심리적인 거리
	case = combinations(Nlist, 3)    # 세 명을 뽑을 조합
	for a, b, c in case:
		dist = 0
		dist += mbti_dist(a, b)
		dist += mbti_dist(b, c)
		dist += mbti_dist(a, c)
		
		res = min(res, dist)
	return res

T = int(input())
for _ in range(T):
	N = int(input())
	Nlist = input().rstrip().split()
	if N > 32:
		print(0)
	else:
		print(find_closest_students(Nlist))