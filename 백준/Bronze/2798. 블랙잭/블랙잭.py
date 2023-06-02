import copy
N,M=map(int,input().split())
temp=list(map(int,input().split()))
cards=copy.deepcopy(temp)
sums=[]
for i in cards:
    cards=copy.deepcopy(temp)
    sum=i
    cards.remove(i)
    for j in cards:
        sum=i+j
        cards.remove(j)
        for k in cards:
            sum=i+j+k
            if sum<=M:
                sums.append(sum)
print(max(sums))