from collections import deque
import sys
import random
input=sys.stdin.readline
N=int(input())
line=deque(list(map(int,input().split())))
line2=deque([])
flag=0
i=1
while line:
    if line[0]==i:
        line.popleft()
        i+=1
    else:
        line2.appendleft(line.popleft())
    while line2:
        if line2[0]==i:
            line2.popleft()
            i+=1
        else:
            break
if len(line)==0 and len(line2)==0:
    print("Nice")
else:
    print("Sad")