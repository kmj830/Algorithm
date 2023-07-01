import math
def gcd(nums):
    a=max(nums)
    b=min(nums)
    while b!=0:
        a,b=b,a%b
    return a
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[a[0]*b[1]+b[0]*a[1],a[1]*b[1]]
gcd=gcd(c)
# gcd=math.gcd(c[0],c[1])
print(c[0]//gcd,c[1]//gcd)