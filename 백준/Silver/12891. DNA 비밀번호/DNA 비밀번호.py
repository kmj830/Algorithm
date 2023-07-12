import sys
input=sys.stdin.readline
S,P=map(int,input().split())
dna=input()
check_list=list(map(int,input().split()))
start=0
now_list=[dna[start:P].count('A'),dna[start:P].count('C'),dna[start:P].count('G'),dna[start:P].count('T')]
count=0
for i in range(P,S+1):
    if now_list[0]-check_list[0]>=0 and now_list[1]-check_list[1]>=0 and now_list[2]-check_list[2]>=0 and now_list[3]-check_list[3]>=0:
        count+=1
    if dna[start]=='A':
        now_list[0]-=1
    elif dna[start]=='C':
        now_list[1]-=1
    elif dna[start]=='G':
        now_list[2]-=1
    else:
        now_list[3]-=1
    start+=1
    if dna[i]=='A':
        now_list[0]+=1
    elif dna[i]=='C':
        now_list[1]+=1
    elif dna[i]=='G':
        now_list[2]+=1
    else:
        now_list[3]+=1
print(count)