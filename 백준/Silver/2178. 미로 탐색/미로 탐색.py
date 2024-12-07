# 문제 27 / 미로 탐색
# https://www.acmicpc.net/problem/2178
# 임시저장 : 튜플 리스트로 바꿔서 해보기
from collections import deque
import sys
input=sys.stdin.readline
def bfs():
  visited[0][0]=True
  queue=deque([[0,0]])
  while queue:
    tmp=queue.popleft()
    if tmp==[n-1,m-1]:
      return maze[n-1][m-1]
    coord=findone(tmp[0],tmp[1])
    for i in coord:
      queue.append(i)
      maze[i[0]][i[1]]=maze[tmp[0]][tmp[1]]+1
      visited[i[0]][i[1]]=True
def findone(i,j):
  found=[]
  try:
    if maze[i+1][j]!=0 and not visited[i+1][j]:
      found.append([i+1,j])
  except:
    pass
  try:
    if maze[i][j+1]!=0 and not visited[i][j+1]:
      found.append([i,j+1])
  except:
    pass
  try:
    if maze[i-1][j]!=0 and not visited[i-1][j] and i>0:
      found.append([i-1,j])
  except:
    pass
  try:
    if maze[i][j-1]!=0 and not visited[i][j-1] and j>0:
      found.append([i,j-1])
  except:
    pass
  return found
n,m=map(int,input().split())
visited=[[False for _ in range(m)] for _ in range(n)]
maze=[]
for _ in range(n):
  maze.append(list(map(int,list(input().strip()))))
print(bfs())