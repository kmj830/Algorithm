M=int(input())
constructor=[i for i in range(1,M) if i+sum(map(int,str(i)))==M]
try:
    print(min(constructor))
except:
    print(0)