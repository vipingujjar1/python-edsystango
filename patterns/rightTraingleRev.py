rows=int(input("Enter how many rows do you want :"))

count=rows

for i in range(rows):
    for k in range(count-1):
        print(end=' ')

    count-=1

    for j in range(i+1):
        print("*",end='')
    print()
