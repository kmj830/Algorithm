import sys
for _ in range(int(input())):
    temp=input()
    stack=[]
    for i in temp:
        if i == "(":
            stack.append(i)
        else:
            try:
                stack.pop()
            except:
                print("NO")
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")