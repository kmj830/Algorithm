n,taesoo,p=map(int,input().split())
if n==0:
    print(1)
else:
    rank=list(map(int,input().split()))
    if n==p and rank[-1]>=taesoo:
        print(-1)
    else:
        count=n+1
        for i in range(n):
            if rank[i]<=taesoo:
                count=i+1
                break
        print(count)