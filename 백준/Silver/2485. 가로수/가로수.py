import sys
import math
n=int(sys.stdin.readline().strip())
array=[]
for _ in range(n):
    array.append(int(sys.stdin.readline().strip()))
steps=[array[i+1]-array[i] for i in range(n-1)]
step=math.gcd(*steps)
count=0
for i in steps:
    count+=i//step-1
print(count)