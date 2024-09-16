# Binary of ASCII char
bit=8
#cha='A'
char=input("enter character:\n")
ch=ord(char)
while bit>=0:
    if ch & (1<<bit):
        print("1")
    else:
        print("0")
    bit=bit-1
print("\n")
