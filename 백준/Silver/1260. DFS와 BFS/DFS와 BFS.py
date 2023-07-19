import sys
from collections import deque
input=sys.stdin.readline
n,m,start=map(int,input().split())
array=[[] for _ in range(n+1)]
dfs_visited=[False]*(n+1)
bfs_visited=[False]*(n+1)
dfs_route=[]
bfs_route=[]

def DFS(v):
    dfs_visited[v]=True
    dfs_route.append(v)
    for i in array[v]:
        if not dfs_visited[i]:
            DFS(i)


def BFS(v):
    queue=deque()
    queue.append(v)
    bfs_visited[v]=True
    while queue:
        now_Node=queue.popleft()
        bfs_route.append(now_Node)
        for i in array[now_Node]:
            if not bfs_visited[i]:
                bfs_visited[i]=True
                queue.append(i)


for _ in range(m):
    s,e=map(int,input().split())
    array[s].append(e)
    array[e].append(s)
for i in range(n+1):
    array[i].sort()
DFS(start)
for i in dfs_route:
    print(i,end=" ")
BFS(start)
print()
for i in bfs_route:
    print(i,end=" ")