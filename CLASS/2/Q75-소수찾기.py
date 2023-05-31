m, n = map(int, input().split())

nums = [True] * (n+1)
nums[0] = nums[1] = False

for i in range(2, int(n**0.5)+1):
    if nums[i] == True:
        for j in range(i+i, n+1, i):
            nums[j] = False

for i in range(m, n+1):
    if nums[i] == True:
        print(i)


# m, n = map(int,input().split())

# for i in range(m,n+1):
#     if i==1:
#         continue
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0:
#             break
#     else:
#         print(i)

