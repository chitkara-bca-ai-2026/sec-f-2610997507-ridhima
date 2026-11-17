
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
    

print(lines,words,char)