import sys
n=int(input())
array=set()
for i in range(n):
    temp=sys.stdin.readline().split()
    if temp[1]=="enter":
        array.add(temp[0])
    else:
        array.discard(temp[0])
for i in sorted(array,reverse=True):
    print(i)