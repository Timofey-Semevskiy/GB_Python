def my_func(x,y):
    x = x ** y
    return x 

x = abs(int(input("Enter num: ")))
y = abs(int(input("Enter pow: ")))

print(my_func(x,y))