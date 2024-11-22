from sys import stdin
input=stdin.readline
stk=[];answer=[];cur=1
for _ in range(int(input())):
  num=int(input())
  while cur<=num:
    stk.append(cur)
    cur+=1
    answer.append('+')
  if stk[-1]==num:
    stk.pop()
    answer.append('-')
  else:
    print('NO')
    break
else:
  for i in answer:
    print(i)