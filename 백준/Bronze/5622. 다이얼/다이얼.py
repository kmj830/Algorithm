time=0
for i in input():
    num="ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(i)
    if 0<=num<3:
        time+=3
    elif 3<=num<6:
        time+=4
    elif 6<=num<9:
        time+=5
    elif 9<=num<12:
        time+=6
    elif 12<=num<15:
        time+=7
    elif 15<=num<19:
        time+=8
    elif 19<=num<22:
        time+=9
    elif 22<=num<26:
        time+=10
print(time)