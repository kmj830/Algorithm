n,m=map(int,input().split())
s=[]
record=[]
def dfs():
    if len(s)==m and sorted(s) not in record:
        print(' '.join(map(str,s)))
        record.append(sorted(s))
        return
    
    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
dfs()