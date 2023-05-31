S = input().lower()
New_S = [0]*26
for i in S:
    New_S[ord(i)-97] += 1
MAX_TRUE = 0
for i in New_S:
    if i == max(New_S):
        MAX_TRUE += 1
if MAX_TRUE == 1:
    print(chr(New_S.index(max(New_S))+65))
else:
    print('?')


S = input().lower()
New_S = [0]*26
for i in S:
    New_S[ord(i)-97] += 1
if New_S.count(max(New_S)) >=2:
    print('?')
else :
    print(chr(New_S.index(max(New_S))+65))
