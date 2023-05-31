M=int(input());N=int(input())
pn=[]
for i in range(M,N+1):
    count=0
    if i>1:
        for j in range(2,i):
            if i%j==0:
                count+=1
        if count==0:
            pn.append(i)
if len(pn)>0:
    print(sum(pn))
    print(sorted(pn)[0])
else:
    print(-1)