num=int(input("enter num1:\n"))
lst=9
hgt=0
while num>0:
    res=num%10
    if res>=hgt:
        hgt=res
    elif res<=lst:
        lst=res
    num//=10
print("highest:\n",hgt)
print("lowest:\n",lst)
