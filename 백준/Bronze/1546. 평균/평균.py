N=int(input())
scores=list(map(int,input().split()))
fakescores=list(map(lambda x:x/max(scores)*100,scores))
print(sum(fakescores)/N)