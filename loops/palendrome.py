num=int(input("Enter no. :"))

value=num

j=10**(len(str(num))-1)
numRev=0

for i in range(num):
    temp=num%10
    numRev+=temp*j
    num=num//10
    j=j/10

if numRev==value:
    print("{} is a palendrome".format(value))
else:
    print("{} is not a palendrome".format(value))
