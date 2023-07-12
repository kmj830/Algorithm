n=int(input())
start,end=1,1
count,sum=0,1
while True:
    if sum==n:
        count+=1
        if start==end:
            break
        sum-=start
        start+=1
    elif sum<n:
        end+=1
        sum+=end
    else:
        sum-=start
        start+=1
print(count)