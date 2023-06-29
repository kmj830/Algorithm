n,m=map(int,input().split())
import sys
result=[]
temp=[sys.stdin.readline().rstrip() for i in range(n)]
for i in range(n-7):
    for j in range(m-7):
        count=0
        flag='W'
        for c in range(i,i+8):
            for r in range(j,j+8):
                if temp[c][r]!=flag:
                    count+=1
                if flag=='B':
                        flag='W'
                else:
                    flag='B'
            if flag=='B':
                flag='W'
            else:
                flag='B'
        result.append(count)
        flag='B'
        count=0
        for c in range(i,i+8):
            for r in range(j,j+8):
                if temp[c][r]!=flag:
                    count+=1
                if flag=='B':
                        flag='W'
                else:
                    flag='B'
            if flag=='B':
                flag='W'
            else:
                flag='B'
        result.append(count)
print(min(result))