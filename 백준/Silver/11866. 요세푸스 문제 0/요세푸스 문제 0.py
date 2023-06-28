from collections import deque
N,K=map(int,input().split())
circle=deque(list(range(1,N+1)))
josephus=[]
while circle:
    circle.rotate(-(K-1))
    josephus.append(circle.popleft())
print(f"<{', '.join(map(str,josephus))}>")