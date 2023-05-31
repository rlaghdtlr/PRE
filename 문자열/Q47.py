S = input()
S_list = [-1]*26
for i in S:
    S_list[ord(i)-97] = S.index(i)
print(*S_list)

