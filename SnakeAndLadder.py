left=20
x=60+left
y=40
def printChar(scount,ccount,chr,nl):
    for j in range (scount):
          print(" ",end="")
    for i in range (ccount):
        if nl==1:
             print(chr)
             for j in range (scount):
               print(" ",end="")
        elif nl==0:
          print(chr,end="")
printChar(10,10,"*",0)
print('\n')
printChar(19,5,"*",1)
print('\n')
printChar(10,5,"*",1)


