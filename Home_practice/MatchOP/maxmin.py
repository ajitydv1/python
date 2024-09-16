import operator

num=-5
match num:
    case num if num>0:
        print("+")
    case num if num<0:
        print("-")
    case _:
        print("0")
print(operator.contains("ajeet",'j'))