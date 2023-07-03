# https://www.acmicpc.net/problem/1931
# 문제 127 - 회의실 배정

# ver_1.0
import sys
input = sys.stdin.readline

def max_meetings(n, meetings):
    # 회의를 끝나는 시간 순으로 정렬
    meetings.sort(key=lambda x: (x[1], x[0]))

    count = 1
    end_time = meetings[0][1]  # 첫 번째 회의의 끝나는 시간

    for i in range(1, n):
        start_time, finish_time = meetings[i]
        if start_time >= end_time:  # 이전 회의의 끝나는 시간 이후에 시작하는 회의라면
            count += 1
            end_time = finish_time  # 해당 회의의 끝나는 시간으로 업데이트

    return count

n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]
print(max_meetings(n, meetings))