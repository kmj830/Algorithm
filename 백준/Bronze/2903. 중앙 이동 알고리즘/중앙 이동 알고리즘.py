line=[2]
for i in range(int(input())):
    line.append(((line[i]-1)*2+1))
print(line[-1]**2)