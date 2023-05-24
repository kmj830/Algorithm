N=int(input())
for i in range(1,2*N+1):
    if i<=N:
        s=i*2-1
        temp=" "*(N-i)+"*"*(s)
    else:
        s-=2
        temp=" "*(i-N)+"*"*s
    print(temp)