
lines=0

words=0
char=0


f=open("data.txt","r")


li=f.readlines()
for line in li:
    print(line)
    lines+=1
    words+=len(line.split())
    char+=len(line)

    for ch in line:
        if ch.isalpha():
            alpha+=1
        elif ch.isdigit():
            digit+=1
        elif ch.isspace():
            space+=1
    

print(lines,words,char)
print(alpha,digit,space)