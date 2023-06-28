from collections import deque
for _ in range(int(input())):
    N,M=map(int,input().split())
    docs=deque(list(map(int,input().split())))
    count=0
    while docs:
        best=max(docs)
        front=docs.popleft()
        M-=1
        if best==front:
            count+=1
            if M<0:
                print(count)
                break
        else:
            docs.append(front)
            if M<0:
                M=len(docs)-1