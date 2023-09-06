text=input()
fulltext=[]
for i in range(len(text)):
    for j in range(i,len(text)):
        frag_1=''.join(reversed(text[0:i+1]))
        frag_2=''.join(reversed(text[i+1:j+1]))
        frag_3=''.join(reversed(text[j+1:]))
        if frag_1=='' or frag_2=='' or frag_3=='':
            continue
        else:
            fulltext.append(f"{frag_1}{frag_2}{frag_3}")
fulltext.sort()
print(fulltext[0])