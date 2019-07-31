num=int(input("Enter no. :"))

value=num

j=10**(len(str(num))-1)
sum=0

for i in range(len(str(num))):
    temp=num%10
    sum+=temp**3
    num=num//10
    j=j/10

if value==sum:
    print("{} is an armstrong no.".format(value))
else:
    print("{} is not an armstrong no.".format(value))
