import sys
input=sys.stdin.readline
S,P=map(int,input().split())
dna=input().strip()
acgt=list(map(int,input().split()))
start,end=0,P
temp=[0,0,0,0]
count=0
for i in range(P):
    match dna[i]:
        case 'A':
            temp[0]+=1
        case 'C':
            temp[1]+=1
        case 'G':
            temp[2]+=1
        case 'T':
            temp[3]+=1
while end<=S:
    if temp[0]>=acgt[0] and temp[1]>=acgt[1] and temp[2]>=acgt[2] and temp[3]>=acgt[3]:
        count+=1
    try:
        match dna[start]:
            case 'A':
                temp[0]-=1
            case 'C':
                temp[1]-=1
            case 'G':
                temp[2]-=1
            case 'T':
                temp[3]-=1
        match dna[end]:
            case 'A':
                temp[0]+=1
            case 'C':
                temp[1]+=1
            case 'G':
                temp[2]+=1
            case 'T':
                temp[3]+=1
        start+=1;end+=1
    except:
        break
print(count)