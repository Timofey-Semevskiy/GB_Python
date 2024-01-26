def my_func(v1,v2,v3):
    list = [v1,v2,v3]
    list.sort()
    return list[1] + list[2]


print(my_func(int(input("Enter: first num ")),int(input("Enter: second num ")),int(input("Enter: third num "))))