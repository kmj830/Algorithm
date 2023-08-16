import sys
input=sys.stdin.readline
N=int(input())
meetings=[]
for _ in range(N):
    meetings.append(list(map(int,input().split())))
    if meetings[-1][0]>meetings[-1][1]:
        meetings.pop()
meetings.sort(key=lambda x:(x[1],x[0]),reverse=True)
count=0
while meetings:
    now=meetings.pop()
    while meetings and now[1]>meetings[-1][0]:
        meetings.pop()
    count+=1
print(count)