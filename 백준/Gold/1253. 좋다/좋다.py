N=int(input())
A=list(map(int,input().split()))
A.sort()
count=0
for i in range(N):
    start,end=0,N-1
    while start<end:
        if A[start]+A[end]>A[i]:
            end-=1
        elif A[start]+A[end]<A[i]:
            start+=1
        else:
            if start==i:
                start+=1
            elif end==i:
                end-=1
            else:
                count+=1
                break
print(count)