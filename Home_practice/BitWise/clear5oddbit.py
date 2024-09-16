# clear 5 odd bits
bit=9
num=int(input("enter the data:\n"))
while bit>=1:
    num=num & ~(1<<bit)
    bit=bit-2
print(num)
