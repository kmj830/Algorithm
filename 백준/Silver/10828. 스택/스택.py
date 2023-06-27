import sys
class Stack:
    def __init__(self) -> None:
        self.stack=list()
    def push(self,n):
        self.stack.append(n)
    def pop(self):
        print(self.stack.pop()) if self.stack else print(-1)
    def size(self):
        print(len(self.stack))
    def empty(self):
        print(0) if self.stack else print(1)
    def top(self):
        print(self.stack[-1]) if self.stack else print(-1)
test=Stack()
for _ in range(int(input())):
    temp=sys.stdin.readline().split()
    if temp[0]=="push":
        test.push(int(temp[1]))
    elif temp[0]=="pop":
        test.pop()
    elif temp[0]=="size":
        test.size()
    elif temp[0]=="empty":
        test.empty()
    else:
        test.top()