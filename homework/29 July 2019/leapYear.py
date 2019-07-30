# check if year is leap year or not

year=int(input("Enter the year[yyyy] :"))

if year%400==0:
	print("It is leap year");
elif year%100==0:
	print("It is not a leap year")
elif year%4==0:
	print("It is a leap year")
else:
	print("It is not a leap year")
