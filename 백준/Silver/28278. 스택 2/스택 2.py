import sys
input=sys.stdin.readline
N=int(input())
stack=[]
for _ in range(N):
    temp=list(map(int,input().split()))
    if temp[0]==1:
        stack.append(int(temp[1]))
    elif temp[0]==2:
        try:
            print(stack.pop())
        except:
            print("-1")
    elif temp[0]==3:
        print(len(stack))
    elif temp[0]==4:
        print(0) if stack else print(1)
    elif temp[0]==5:
        try:
            print(stack[-1])
        except:
            print(-1)