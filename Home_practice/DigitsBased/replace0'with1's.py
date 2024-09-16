num=int(input("enter data:\n"))
res=0
rev=0
while num>0:
    temp= 1 if num%10==0 else num%10
    rev=rev*10+temp
    num//=10
while rev>0:
    res=res*10+rev%10
    rev//=10
print(res)

