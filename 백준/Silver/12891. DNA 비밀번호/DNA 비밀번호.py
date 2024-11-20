#03-4 p65

# import sys
# input=sys.stdin.readline
result=0
def check():
  global my_list,acgt,result
  if my_list['A']>=acgt['A'] and my_list['C']>=acgt['C'] and my_list['G']>=acgt['G'] and my_list['T']>=acgt['T']:
    result+=1
s,p=map(int,input().split())
dna=list(input())
temp=list(map(int,input().split()))
acgt={
    'A':temp[0],
    'C':temp[1],
    'G':temp[2],
    'T':temp[3]
}
my_list={
    'A':0,
    'C':0,
    'G':0,
    'T':0
}

for k in range(p):
  my_list[dna[k]]+=1
check()
for i in range(p,s):
  j=i-p
  my_list[dna[j]]-=1
  my_list[dna[i]]+=1
  check()
print(result)