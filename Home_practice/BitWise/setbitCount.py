# coutn set bits of given data
bits=31
cnt=0
data=int(input("enter data:\n"))
while bits>=0:
    if data & 1<<bits:
        cnt=cnt+1
    bits=bits-1
print(cnt)
