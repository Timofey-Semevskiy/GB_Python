num = int(input("Enter number: "))

min_num = -1
while num > 10:
    d = num % 10
    num //= 10
    if d > min_num:
        min_num = d
print(min_num)