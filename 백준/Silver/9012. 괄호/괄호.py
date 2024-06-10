import sys
input=sys.stdin.readline
def vps(ps):
  s=[]
  for i in ps:
    s.append(i)
    try:
      if s[-1]==')' and s[-2]=='(':
        s.pop()
        s.pop()
    except:
      None
  if len(s)==0:
    return 'YES'
  else:
    return 'NO'
for _ in range(int(input())):
  print(vps(input().strip()))