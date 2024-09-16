min=int(input("enter min number:\n"))
max=int(input("enter max number:\n"))
flag=1
for i in range(min,max):
    flag=1
    s=i//2
    for j in range(2,s):
        if i%j==0:
            flag=0
    if flag:
        #print(i)
        temp=i
        res=0
        while temp>0:
            res=res*10+temp%10
            if res==3 or res==7:
                print(temp)
            temp//=10

