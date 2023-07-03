import sys
n=int(input())
ChongChonglist=set();ChongChonglist.add("ChongChong")
for _ in range(n):
    a,b=sys.stdin.readline().split()
    if a in ChongChonglist or b in ChongChonglist:
        ChongChonglist.add(a);ChongChonglist.add(b)
print(len(list(ChongChonglist)))