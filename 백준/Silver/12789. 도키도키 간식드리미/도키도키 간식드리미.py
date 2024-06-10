import sys
input=sys.stdin.readline

from collections import deque

n=int(input())
now=deque(list(map(int,input().split())))
space=[]
wait=[0,0]
result=[]
c=1
while now:
  if len(space)>0:
    wait[1]=space[-1]
  else:
    wait[1]=0
  if len(now)>0:
    wait[0]=now[0]
  else:
    wait[0]=0
  if wait[0]==c:
    result.append(now.popleft())
    c+=1
  elif wait[1]==c:
    result.append(space.pop())
    c+=1
  else:
    space.append(now.popleft())
for _ in range(len(space)):
  result.append(space.pop())
if result==sorted(result):
  print("Nice")
else:
  print("Sad")