n=int(input())

rec_count=0
dp_count=0

dp=[0]*41

def fib(n):
    global rec_count
    a,b=1,1
    for _ in range(3,n+1):
        a,b=b,a+b
    rec_count=b
    return b

def fibwdp(n):
    global dp_count
    dp[1]=dp[2]=1
    for i in range(3,n+1):
        dp_count+=1
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]

fib(n)
fibwdp(n)
print(rec_count,dp_count)