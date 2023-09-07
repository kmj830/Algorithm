import itertools
tc=int(input())
for _ in range(tc):
    n=int(input())
    dic={}
    for i in range(n):
        dressname,dresstype=input().split()
        if dresstype not in dic:
            dic[dresstype]=[dressname]
        else:
            dic[dresstype].append(dressname)
    item=[];count=0
    for i,j in dic.items():
        item.append(len(j))
    result=1
    for i in item:
        result*=(i+1)
    print(result-1)