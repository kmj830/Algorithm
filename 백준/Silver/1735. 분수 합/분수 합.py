import math
# def gcd(nums):
#     a=max(nums)
#     b=min(nums)
#     top=0
#     for i in range(1,b+1):
#         if a%i==0 and b%i==0:
#             top=i
#     return top
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[a[0]*b[1]+b[0]*a[1],a[1]*b[1]]
gcd=math.gcd(c[0],c[1])
print(c[0]//gcd,c[1]//gcd)