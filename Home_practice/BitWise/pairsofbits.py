# pairs of set bit
bit=31
cnt=0
data=int(input("enter data:\n"))
while bit>0:
    if data & 1<<bit:
        if data & (1<<(bit-1)):
            cnt=cnt+1
            bit=bit-1
    bit=bit-1
print(cnt)
