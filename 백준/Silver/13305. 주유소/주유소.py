import sys
input=sys.stdin.readline
N=int(input())
road=list(map(int,input().split()))
city=list(map(int,input().split()));city.pop()
cheap_idx=city.index(min(city))
oil=0;cost=0
for i in range(N-1):
    if oil<road[i]:
        if i==cheap_idx:
            oil+=sum(road[i:])
            cost+=sum(road[i:])*city[i]
        else:
            oil+=road[i]
            cost+=road[i]*city[i]
    oil-=road[i]
print(cost)