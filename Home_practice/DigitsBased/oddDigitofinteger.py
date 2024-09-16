num=int(input("enter digit:\n"))
while num:
    res=num%10
    if res %2:
        print(res,end=" ")
    num//=10

