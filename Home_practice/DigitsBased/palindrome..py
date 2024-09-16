num=int(input("enter data:\n"))
temp=num
res=0
while num>0:
    res=res*10+num%10
    num//=10
if temp==res:
    print("given number is palindrome:",res)
else:
    print("given number is not palindrome:",res)
