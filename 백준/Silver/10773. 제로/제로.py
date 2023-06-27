import sys
stack=[]
for _ in range(int(input())):
    num=int(sys.stdin.readline())
    if num==0:
        stack.pop()
    else:
        stack.append(num)
print(sum(stack))