import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))

def search(arr, n, t):
    arr.sort()
    result = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                total = arr[i] + arr[j] + arr[k]
                if total == t:
                    return total 
                if result < total <= t:
                    result = total
    return result

print(search(cards,n,m))