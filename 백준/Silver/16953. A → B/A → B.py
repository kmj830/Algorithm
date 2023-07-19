import sys
from collections import deque
input=sys.stdin.readline
a,b=map(int,input().split())
answer=[]
def BFS(a,b,count):
    if a>b:
        return
    elif a==b:
        return answer.append(count)
    else:
        BFS(a*2,b,count+1)
        BFS(a*10+1,b,count+1)
BFS(a,b,1)
if answer:
    answer.sort()
    print(answer[0])
else:
    print(-1)