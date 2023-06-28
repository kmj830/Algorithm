from collections import deque
import sys
testdeque=deque([])
for _ in range(int(input())):
    temp=sys.stdin.readline().split()
    if temp[0]=='push_front':
        testdeque.appendleft(int(temp[1]))
    elif temp[0]=='push_back':
        testdeque.append(int(temp[1]))
    elif temp[0]=='pop_front':
        print(testdeque.popleft()) if testdeque else print(-1)
    elif temp[0]=='pop_back':
        print(testdeque.pop()) if testdeque else print(-1)
    elif temp[0]=='size':
        print(len(testdeque))
    elif temp[0]=='empty':
        print(0) if testdeque else print(1)
    elif temp[0]=='front':
        print(testdeque[0]) if testdeque else print(-1)
    else:
        print(testdeque[-1]) if testdeque else print(-1)