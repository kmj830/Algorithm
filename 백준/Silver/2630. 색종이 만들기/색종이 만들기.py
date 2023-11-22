import sys
input=sys.stdin.readline
arr=[]
stk=[]
result=[]
z,o=0,0
for _ in range(int(input())):
    arr.append(list(map(int,input().split())))
stk.append(arr)

def devide(p):
    global o,z
    arr=stk.pop()
    flag=check(arr)
    if flag==2:
        temp=[]
        for i in range(len(arr)//2):
                temp.append(arr[i][0:len(arr)//2])
        stk.append(temp)
        devide(stk)
        temp=[]
        for i in range(len(arr)//2):
            temp.append(arr[i][len(arr)//2:])
        stk.append(temp)
        devide(stk)
        temp=[]
        for i in range(len(arr)//2,len(arr)):
                temp.append(arr[i][0:len(arr)//2])
        stk.append(temp)
        devide(stk)
        temp=[]
        for i in range(len(arr)//2,len(arr)):
            temp.append(arr[i][len(arr)//2:])
        stk.append(temp)
        devide(stk)
        temp=[]
    elif flag==1:
        o+=1
    else:
        z+=1
def check(arr):
    flag=arr[0][0]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if flag!=arr[i][j]:
                return 2
    return flag


devide(stk)
print(z)
print(o)