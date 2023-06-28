import sys
from collections import deque
queue=deque()
for _ in range(int(input())):
    temp=sys.stdin.readline().split()
    if temp[0]=='push':
        queue.append(int(temp[1]))
    elif temp[0]=='pop':
        print(queue.popleft()) if queue else print(-1)
    elif temp[0]=='size':
        print(len(queue))
    elif temp[0]=='empty':
        print(0) if queue else print(1)
    elif temp[0]=='front':
        print(queue[0]) if queue else print(-1)
    else:
        print(queue[-1]) if queue else print(-1)