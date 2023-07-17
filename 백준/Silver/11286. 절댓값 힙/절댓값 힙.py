import sys
from queue import PriorityQueue
input=sys.stdin.readline
n=int(input())
que=PriorityQueue()
answer=[];count=0
for _ in range(n):
    x=int(input())
    if x!=0:
        que.put((abs(x),x))
        count+=1
    else:
        if count>0:
            answer.append(que.get()[1])
            count-=1
        else:
            answer.append(0)
for i in answer:
    print(i)