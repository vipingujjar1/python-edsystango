rows=int(input("Enter no. of rows you want :"))

temp=0
count=(rows*2)+1

for i in range(rows+1):
    for j in range(temp):
        print(end=' ')

    temp+=1

    for k in range(count):
        print('*',end='')

    count-=2
    print('')
