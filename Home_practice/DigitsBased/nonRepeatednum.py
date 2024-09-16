num=int(input("enter data:\n"))
temp=0
res=0
n=num
while num>0:
    res=res*10+num%10
    while n:
        if res==n%10: