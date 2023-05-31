# S = input()
# C_list = ['c=', 'c-', 'd-', 'lj', 'nj', 's=']
# count = 0
# out = 0
# for i in range(len(S)):
#     if (i < len(S) - 2 and S[i:i+3] == 'dz='):
#         count += 1
#         out += 3
#     elif i < len(S) - 1 and S[i:i+2] in C_list:
#         count += 1
#         out += 2
#     elif (i < len(S) - 1 and S[i:i+2] == 'z=') and ((i < len(S) - 1 and S[i-1:i+2] != 'dz=')):
#         count += 1
#         out += 2
# print(count+len(S)-out)

S = input()
C_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in C_list:
    S = S.replace(i,'*')
print(len(S))