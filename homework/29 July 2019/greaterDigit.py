# find greater digit from three digit no.

num1=int(input("Enter a three digit no. :"))

for i in range(3):
    if i==0:
        max=num1%10
        num1=num1//10
    else:
        temp=num1%10
        if temp>max:
            max=temp
        num1=num1//10

print(max)
