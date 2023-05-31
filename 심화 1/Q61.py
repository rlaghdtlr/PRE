N = int(input())
A = N

for i in range(N) :
    word = input()
    for j in range(len(word)-1) :
        if word[j] == word[j+1] :
            continue
        elif word[j] in word[j+1:] :
            A -= 1
            break
print(A)


N = int(input())
cnt = 0
for _ in range(N):
    word = input().strip()
    if list(word) == sorted(word,key=word.find):
        cnt += 1
print(cnt)


# N = int(input())
# A = N
# for _ in range(N):
#     S = input()
#     T = [0]
#     for i in S:
#         try:
#             if T.index(i) ==True and T[-1] == i:
#                 T.append(i)
#             elif T.index(i) ==True and T[-1] != i:
#                 A -=1
#                 break
#         except:
#             T.append(i)
# print(A)


N = int(input())
A = N
for _ in range(N):
    S = input()
    T = []
    for i in S:
        if i in T and T[-1] == i:
            T.append(i)
        elif i in T and T[-1] != i:
            A -= 1
            break
        else:
            T.append(i)
print(A)