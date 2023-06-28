from collections import deque
import sys
for _ in range(int(input())):
    p=sys.stdin.readline().rstrip()
    n=int(input())
    array=deque(eval(input()))
    flag=0
    for i in p:
        if i=='R':
            flag+=1
        else:
            if array:
                if flag%2==0:
                    array.popleft()
                else:
                    array.pop()
            else:
                print("error")
                break
    else:
        array.reverse() if flag%2!=0 else None
        print(f"[{','.join(list(map(str,array)))}]")