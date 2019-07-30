# marksheet programm

maths=int(input("Enter marks obtain in maths :"))
physics=int(input("Enter marks obtain in physics :"))
chemistry=int(input("Enter marks obtain in chemistry :"))
communication=int(input("Enter marks obtain in communication :"))
computer=int(input("Enter marks obtain in computer :"))

total=maths+physics+chemistry+communication+computer
percent=total/5

if percent>=60:
    print("Congratulation you have got first grade.")
elif percent > 50 and percent<60:
    print("You have got second grade, you need to work harder.")
elif percent>=35 and percent<=50:
    print("You have got third grade, really poor work.")
else:
    print("You are fail, you are not allowed to sit in new class.")
