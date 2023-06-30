n=int(input())
import sys
array=[]
for i in range(n):
    array.append(int(sys.stdin.readline().rstrip()))
array=sorted(list(set(array)))
for i in array:
    print(i)