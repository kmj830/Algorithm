import sys
n=int(input())
chat=[]
for i in range(n):
    chat.append(sys.stdin.readline().strip())
temp=set();count=0
for i in chat:
    if i=="ENTER":
        count+=len(list(temp))
        temp=set()
    else:
        temp.add(i)
count+=len(list(temp))
print(count)