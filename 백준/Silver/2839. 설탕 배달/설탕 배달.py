n=int(input())
count=0
while n%5!=0:
    count+=1
    n-=3
if n>=0:
    count+=n//5
    print(count)
else:
    print(-1)