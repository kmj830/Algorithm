from collections import deque
import sys
input=sys.stdin.readline
N=int(input())
deq=deque(enumerate(map(int,input().split()),start=1))
ans=[]
while deq:
    index,balloon=deq.popleft()
    ans.append(index)
    if balloon>0:
        deq.rotate(-(balloon-1))
    elif balloon<0:
        deq.rotate(-balloon)
print(' '.join(map(str,ans)))