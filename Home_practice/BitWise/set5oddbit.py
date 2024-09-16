# set 5 0dd bits from start
bit=9
num=int(input("enter the data:"))
while bit>=1:
    num=num|(1<<bit)
    bit=bit-2
print(num)
