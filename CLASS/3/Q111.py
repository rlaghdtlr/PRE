# n = input()
# num_N = int(n)
# count = 0
# while num_N > 0:
#     if (sum(map(int, n)) % 3) == 0:
#         num_N //= 3
#     elif (int(n[-1]) % 2) == 0:
#         num_N //= 2
#     else:
#         num_N -= 1
#     n = str(num_N)
#     count += 1
#     if num_N == 1:
#         break
# print(count)


def make_1(n):
    cnt = [0] * (n + 1)
    for i in range(2, n + 1):
        cnt[i] = cnt[i - 1] + 1
        if i % 2 == 0:
            cnt[i] = min(cnt[i], cnt[i // 2] + 1)
        if i % 3 == 0:
            cnt[i] = min(cnt[i], cnt[i // 3] + 1)
    return cnt[n]
n = int(input())
print(make_1(n))

