import sys
n=int(sys.stdin.readline().strip())
array=[0]*10001
for i in range(n):
    array[int(sys.stdin.readline().strip())]+=1
for i in range(len(array)):
    for j in range(array[i]):
        print(i)