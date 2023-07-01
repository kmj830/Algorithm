def gcd(nums):
    a=max(nums)
    b=min(nums)
    top=0
    for i in range(1,b+1):
        if a%i==0 and b%i==0:
            top=i
    return top
def lcm(nums):
    a=max(nums)
    b=min(nums)
    return a*b//gcd(nums)

nums=list(map(int,input().split()))
print(lcm(nums))