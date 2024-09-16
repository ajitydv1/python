hgt=0
shgt=0
num=int(input("enter data:\n"))
while num>0:
    res=num%10
    if res>=hgt:
        shgt=hgt
        hgt=res
    elif res>shgt and shgt!=hgt:
        shgt=res
    num//=10
print("second highest:\n",shgt)
