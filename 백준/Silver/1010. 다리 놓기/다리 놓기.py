import sys
import math
t=int(sys.stdin.readline().strip())
for _ in range(t):
    n,m=map(int,sys.stdin.readline().strip().split())
    mPn=math.factorial(m)//(math.factorial(m-n)*math.factorial(n))
    print(mPn)