C=int(input())
for i in range(C):
    count,*scores=map(int,input().split())
    avg=sum(scores)/count
    up=[]
    for score in scores:
        if score > avg:
            up.append(score)
    print(f"{len(up)/len(scores)*100:.3f}%")