list = [1,2,3,4,5,6,7,8,9,10,11,12]
inputNum  = int(input("Enter num: "))

if inputNum in list[0:4]:
    print("Winter")
elif inputNum in list[4:7]:
    print("Spring")
elif inputNum in list[7:10]:
    print("Summer")
elif inputNum in list[10:]:
    print("Autumn")
else:
    print("Invalid input")

