import sys
testcase=int(input())
s=set()

for i in range(testcase):
    input_text=sys.stdin.readline().strip().split()
    
    if len(input_text)==1:
        if input_text[0]=='all':
            s=set([_ for _ in range(1,21)])
        else:
            s=set()
        continue

    command,value=input_text[0],input_text[1]
    value=int(value)


    if command=="add":
        s.add(value)
    if command=="remove":
        s.discard(value)
    if command=="check":
        print(1 if value in s else 0)
    if command=="toggle":
        if value in s:
            s.discard(value)
        else:
            s.add(value)