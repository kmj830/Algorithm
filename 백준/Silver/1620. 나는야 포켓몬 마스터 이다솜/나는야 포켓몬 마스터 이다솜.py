import sys
n,m=map(int,input().split())
pocketmon={};new_pocketmon={}
for i in range(1,n+1):
    pocketmon[i]=sys.stdin.readline().strip()
for k,v in pocketmon.items():
    new_pocketmon[v]=k
for i in range(m):
    temp=sys.stdin.readline().strip()
    if temp.isdigit():
        print(pocketmon[int(temp)])
    else:
        print(new_pocketmon[temp])