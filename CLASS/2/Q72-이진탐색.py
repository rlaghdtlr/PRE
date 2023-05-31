#이진탐색 함수
#리스트, 타겟값, 스타트, 엔드값 인수로 사용
import sys
input = sys.stdin.readline

def search(arr, t, s, e):
    while s <= e:
        mid = (s+e)//2
        cut = 0
        for i in arr:
            cut +=i // mid
        if cut >= t:
            s = mid+1
        else:
            e = mid-1
    return e

k, n = map(int, input().split())
line = [int(input().rstrip()) for _ in range(k)]

print(search(line, n, 1, max(line)))

