rows=int(input("Enter how many rows do you want :"))

for i in range(rows):
    for j in range(i+1):
        print("*",end='')
    print()
