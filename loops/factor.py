num=int(input("Enter a num :"))

count=2

while num!=1:
    if num%count==0:
        num=num/count
        print(num)
        print(count)
        count=2
    count+=1
