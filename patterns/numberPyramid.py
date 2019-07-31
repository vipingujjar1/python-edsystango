rows=int(input("Enter no. of rows you want :"))

temp=rows
count=1

for i in range(rows):
    for j in range(temp):
        print(end=' ')

    temp-=1

    for k in range(count):
        print(i+1,end='')

    count+=2
    print('')
