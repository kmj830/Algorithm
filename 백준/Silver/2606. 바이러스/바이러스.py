import sys
from collections import deque
input=sys.stdin.readline
def BFS():
    global count
    while queue:
        node=queue.popleft()
        for i in array[node]:
            if visited[i]==False:
                queue.append(i)
                visited[i]=True
                count+=1
n=int(input())
m=int(input())
array=[[] for _ in range(n+1)]
visited=[False]*(n+1)
route=[]

for _ in range(m):
    s,e=map(int,input().split())
    array[s].append(e)
    array[e].append(s)
count=0

queue=deque([1])
visited[1]=True
route.append(1)
BFS()
print(count)