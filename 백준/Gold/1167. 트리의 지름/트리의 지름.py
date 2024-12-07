from collections import deque
import sys
input=sys.stdin.readline
def bfs(num):
  queue=deque()
  queue.append(num)
  visited[num]=True
  while queue:
    e=queue.popleft()
    for i in tree[e]:
      if not visited[i[0]]:
        queue.append(i[0])
        visited[i[0]]=True
        distance[i[0]]= distance[e]+i[1]

v=int(input())
tree=[[] for _ in range(v+1)]
visited=[False]*(v+1)
distance=[0]*(v+1)
for _ in range(v):
  tmp=list(map(int,input().split()))
  n=tmp[0]
  for i in range(1,len(tmp),2):
    try:
      tree[n].append((tmp[i],tmp[i+1]))
    except:
      pass
bfs(1)
max_idx=distance.index(max(distance))
visited=[False]*(v+1)
distance=[0]*(v+1)
bfs(max_idx)
print(max(distance))