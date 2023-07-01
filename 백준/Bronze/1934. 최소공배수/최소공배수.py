def lcm(x,y):
    return (x*y)/gcd(x,y)
def gcd(x,y):
    r=1
    while r!=0:
        r=x%y
        x=y;y=r
    return x
testcase=int(input())
a=[0 for col in range(testcase)]; b=[0 for col in range(testcase)]; c=[0 for col in range(testcase)]
for i in range(testcase):
    a[i],b[i]=map(int,input().split())
    c[i]=lcm(a[i],b[i])
for j in range(testcase):
    print(int(c[j]))