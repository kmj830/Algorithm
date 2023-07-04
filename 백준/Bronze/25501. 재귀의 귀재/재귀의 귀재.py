import sys
def recursion(word,l,r,count=0):
    count+=1
    if l>=r:
        return f"1 {count}"
    elif word[l]!=word[r]:
        return f"0 {count}"
    else:
        return recursion(word,l+1,r-1,count)

def isPalindrome(word):
    return recursion(word,0,len(word)-1) 

t=int(sys.stdin.readline())
for _ in range(t):
    word=sys.stdin.readline().strip()
    print(isPalindrome(word))