num=int(input("Enter value of num :"))

first,second=0,1

print(first)
print(second)

for i in range(num):
    print(first+second)
    temp=first
    first=second
    second=first+temp
