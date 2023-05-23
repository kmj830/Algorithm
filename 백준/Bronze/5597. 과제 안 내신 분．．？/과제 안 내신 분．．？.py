numlist=[i+1 for i in range(30)]
for i in range(28):
    numlist.remove(int(input()))
print(f"{sorted(numlist)[0]}\n{sorted(numlist)[1]}")