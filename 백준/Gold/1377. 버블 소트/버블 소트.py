import sys
input=sys.stdin.readline
N=int(input())
array=[]
for i in range(N):
    array.append([int(input()),i])
array.sort()
top=0
for i in range(N):
    if array[i][1]-i>top:
        top=array[i][1]-i
print(top+1)