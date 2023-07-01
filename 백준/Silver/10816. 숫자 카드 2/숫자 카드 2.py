import sys
n=input()
n_nums=sys.stdin.readline().split()
array={}
for i in n_nums:
    if i in array:
        array[i]+=1
    else:
        array[i]=1
m=input()
m_nums=sys.stdin.readline().split()
for i in m_nums:
    try:
        print(array[i],end=" ")
    except:
        print(0,end=" ")