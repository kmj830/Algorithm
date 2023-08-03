from collections import deque
import sys
input=sys.stdin.readline
N=int(input())
deq=deque([])
for _ in range(N):
    temp=input().split()
    if temp[0]=="1":
        deq.appendleft(int(temp[1]))
    elif temp[0]=="2":
        deq.append(int(temp[1]))
    elif temp[0]=="3":
        try:
            print(deq.popleft())
        except:
            print(-1)
    elif temp[0]=="4":
        try:
            print(deq.pop())
        except:
            print(-1)
    elif temp[0]=="5":
        print(len(deq))
    elif temp[0]=="6":
        print(0) if deq else print(1)
    elif temp[0]=="7":
        print(deq[0]) if deq else print(-1)
    else:
        print(deq[-1]) if deq else print(-1)