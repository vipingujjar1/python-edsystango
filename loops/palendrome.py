num=int(input("Enter no. :"))

j=10**len(str(num))
numRev=0

for i in range(num):
    temp=num%10
    numRev+=temp*j
    num=num//10
    j=j/10

print(num)
print(numRev)
