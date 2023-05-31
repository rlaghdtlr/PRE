# def hash_f(n,s):
#     _sum = 0
#     r = 31
#     m = 1234567891
#     for i in range(n):
#         _sum += ((ord(s[i])-96)*(r**i))%m
#     return _sum
# n = int(input())
# print(hash_f(n,input()))


def hash_f(n, s):
    r = 31
    m = 1234567891
    _sum = sum((ord(s[i])-96)*(r**i) for i in range(n))
    return _sum % m

n = int(input())
s = input().strip()

print(hash_f(n, s))

