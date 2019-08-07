num=int(input("Enter no. :"))
i=1

def tabel(i, num):
    if(i>10):
        return 1;
    print("{} * {} = {}".format(num, i, num*i))
    tabel(i+1, num)

tabel(i, num)
