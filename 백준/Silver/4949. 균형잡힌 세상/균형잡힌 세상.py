import sys
input=sys.stdin.readline

def vps(ps):
  s=[]
  for i in ps:
    if i=='(' or i==')' or i=='[' or i==']':
      s.append(i)
    try:
      if (s[-1]==')' and s[-2]=='(') or (s[-1]==']' and s[-2]=='['):
        s.pop()
        s.pop()
    except:
      None
  if len(s)==0:
    return 'yes'
  else:
    return 'no'
while True:
  temp=input().rstrip()
  if temp=='.':
    break
  else:
    print(vps(temp))