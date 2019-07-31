rows=int(input("Enter no. of rows you want :"))

temp=rows
count=1
revTemp=0
revCount=(rows*2)+1
printCount=rows+1

for i in range(rows):
    for j in range(temp):
        print(end=' ')

    temp-=1

    for k in range(count):
        print(i+1,end='')

    count+=2
    print('')

for i in range(rows+1):
    for j in range(revTemp):
        print(end=' ')

    revTemp+=1

    for k in range(revCount):
        print(printCount,end='')

    revCount-=2
    printCount-=1
    print('')
