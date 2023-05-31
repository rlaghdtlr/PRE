n, k = map(int, input().split())
nlist = [i for i in range(1, n+1)]
result = []
while nlist:
    if len(nlist)>=k:
        nlist = nlist[k-1:]+nlist[:k-1]
        result.append(nlist[0])
        del nlist[0]
    else:
        nlist = nlist[k%len(nlist)-1:]+nlist[:k%len(nlist)-1]
        result.append(nlist[0])
        del nlist[0]
print('<' + ', '.join(map(str, result)) + '>')


