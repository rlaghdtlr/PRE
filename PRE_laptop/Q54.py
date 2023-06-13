S = list(map(int, input().split()))
N = [1,1,2,2,2,8]
for i in range(len(S)):
    print(N[i]-S[i],end=' ')

