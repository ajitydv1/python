# longest series of 1's of given data
bit=31
prv=0
crnt=0
cnt=0
data=int(input("enter data:\n"))
while bit>=0:
    if data & 1<<bit:
        cnt=cnt+1
        crnt=cnt
    else:
        cnt=0
    if crnt>=prv:
        prv=crnt
    bit=bit-1
print(prv)
