text=[]
vowel=['a','e','i','o','u']
while True:
    textinput=input()
    if textinput=="end":
        break
    text.append(textinput)
check=[0 for _ in range(len(text))]



for i in range(len(text)):
    if "a" not in text[i] and "e" not in text[i] and "i" not in text[i] and "o" not in text[i] and "u" not in text[i]:
        check[i]=1
        continue
    for j in range(len(text[i])-2):
        if text[i][j] in vowel and text[i][j+1] in vowel and text[i][j+2] in vowel:
            check[i]=1
            continue
        elif text[i][j] not in vowel and text[i][j+1] not in vowel and text[i][j+2] not in vowel:
            check[i]=1
            continue
    for j in range(len(text[i])-1):
        if text[i][j]!="e" and text[i][j]!="o":
            if text[i][j]==text[i][j+1]:
                check[i]=1
                continue


for i in range(len(text)):
    if check[i]==0:
        print(f"<{text[i]}> is acceptable.")
    else:
        print(f"<{text[i]}> is not acceptable.")