#p145

import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
arrive=False
def dfs(v,depth):
  global arrive
  if depth==5:
    arrive=True
    return
  visited[v]=True
  for i in a[v]:
    if not visited[i]:
      dfs(i,depth+1)
  visited[v]=False

n,m=map(int,input().split())
a=[[] for _ in range(n+1)]
visited=[False]*(n+1)
for _ in range(m):
  temp_a,temp_b=map(int,input().split())
  a[temp_a].append(temp_b)
  a[temp_b].append(temp_a)
for i in range(n):
  dfs(i,1)
  if arrive:
    break
if arrive:
  print(1)
else:
  print(0)