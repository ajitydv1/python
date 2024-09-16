# product of given digit
num=int(input("enter digit:\n"))
result=1
if num==0:
    print("product of given digit:\n",num*result)
else:
    if num>0:
        while num:
            result*=num%10
            num//=10
        print("product of given digit:\n",result)
    else:
        num1=num if num>0 else -num
        while num1:
            result*=num1%10
            num1//=10
        print("product of given digit:\n",-result)
