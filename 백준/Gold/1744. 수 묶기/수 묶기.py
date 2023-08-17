import sys
from collections import deque
input=sys.stdin.readline
N=int(input())
array=[[],[]]
for i in range(N):
    num=int(input())
    if num>0:
        array[0].append(num)
    else:
        array[1].append(num)
array[0].sort(reverse=True)
array[1].sort()
array[0]=deque(array[0])
array[1]=deque(array[1])
answer=[]
i=0
while True:
    if len(array[0])>=2:
        a,b=array[0].popleft(),array[0].popleft()
        if a<2:
            answer.append(a)
            array[0].appendleft(b)
        elif b<2:
            answer.append(b)
            array[0].appendleft(a)
        else:
            answer.append(a*b)
    else:
        while array[0]:
            answer.append(array[0].popleft())
        break
while True:
    if len(array[1])>=2:
        a,b=array[1].popleft(),array[1].popleft()
        answer.append(a*b)
    else:
        while array[1]:
            answer.append(array[1].popleft())
        break
print(sum(answer))