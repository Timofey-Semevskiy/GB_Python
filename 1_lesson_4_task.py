km = int(input("Enter km: "))
result = int(input("Enter result what u want : "))
days = 1

while km <= result:
    km = km + (km * 0.1) 
    days = days + 1
    

print(days)
