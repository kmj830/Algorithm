import sys
n,m=map(int,input().split())
dic={}
for _ in range(n):
    word=sys.stdin.readline().strip()
    if len(word) >= m:
        if word in dic:
            dic[word]+=1
        else:
            dic[word]=1
arr=[*dic.items()]
arr.sort(key=lambda x:(-x[1],-len(x[0]),x[0]))
for i in arr:
    print(i[0])