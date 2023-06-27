import re
while True:
    test=input()
    temp=list(test)
    stack=[];count=0
    if temp==['.']:
        break
    for i in temp:
        if i=="(" or i=="[":
            stack.append(i)
        elif i==")":
            if not stack or stack[-1] =="[":
                count+=1
                break
            elif stack[-1]=="(":
                stack.pop()
        elif i=="]":
            if not stack or stack[-1]=="(":
                count+=1
                break
            elif stack[-1]=="[":
                stack.pop()
    else:
        if stack:
            count+=1
    print("yes") if count==0 else print("no")
