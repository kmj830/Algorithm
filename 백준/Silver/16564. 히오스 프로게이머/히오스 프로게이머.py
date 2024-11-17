#16564 이분탐색

import sys
input=sys.stdin.readline
n,k=map(int,input().split())
x=[]
for _ in range(n):
  x.append(int(input()))
x.sort(reverse=True)
nest=1
while k>0 and len(x)>1:
  if (x[-2]-x[-1])*nest<=k:
    k-=(x[-2]-x[-1])*nest
    nest+=1
    x.pop()
  else:
    break
x[-1]+=k//nest
print(x[-1])