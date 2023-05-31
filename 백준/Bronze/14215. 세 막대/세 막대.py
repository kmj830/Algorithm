line=sorted(list(map(int,input().split())))
while line[0]+line[1]<=line[2]:
    line[2]-=1
print(sum(line))