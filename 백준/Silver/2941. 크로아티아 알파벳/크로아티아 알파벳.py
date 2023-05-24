croa=['c=','c-','dz=','d-','lj','nj','s=','z=']
import re
temp=input()
for i in croa:
    temp=re.sub(i," ",temp)
print(len(temp))