import sys
stack=[];answer=[];cur=1
for _ in range(int(input())):
    num=int(sys.stdin.readline())
    while cur<=num:
        stack.append(cur)
        answer.append("+")
        cur+=1
    if stack[-1]==num:
        stack.pop()
        answer.append("-")
    else:   
        print("NO")
        break
else:
    for i in answer:
        print(i)