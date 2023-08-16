import sys
input=sys.stdin.readline
N=int(input())
meetings=[]
for _ in range(N):
    meetings.append(list(map(int,input().split())))
meetings.sort(key=lambda x:(x[1],x[0]))
count=0
lastend=0
# while meetings:
#     now=meetings.pop()
#     while meetings and now[1]>meetings[-1][0]:
#         meetings.pop()
#     count+=1
for times in meetings:
    if times[0]>=lastend:
        count+=1
        lastend=times[1]
print(count)