n=int(input())
start,end=1,0
answer=[]
total=0
while True:
    if total<n:
        end+=1
        total+=end
    elif total>n:
        total-=start
        start+=1
    else:
        answer.append([start,end])
        if start==n and end==n:
            break
        else:
            end+=1
            total+=end
print(len(answer))