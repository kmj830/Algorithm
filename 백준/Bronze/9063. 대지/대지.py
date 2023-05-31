N=int(input())
coordinate=[[],[]]
for i in range(N):
    x,y=map(int,input().split())
    coordinate[0].append(x)
    coordinate[1].append(y)
print((sorted(coordinate[0])[-1]-sorted(coordinate[0])[0])*(sorted(coordinate[1])[-1]-sorted(coordinate[1])[0]))