profit = int(input("Enter profit: "))
ne_profit = int(input("Enter lost: "))


profit_check = profit - ne_profit


if profit_check > 0:
    print(f"profit is {profit_check}")
    viruchka = int(input("Enter viruchka: "))
    renta = (profit_check) / viruchka
    if renta > 0:
        print(f"viruchka is {renta}")
        employees = int(input("Enter employees: "))
        print(f"employees profit: {viruchka / employees}")

    else:
        print("УВЫ") 
        
elif profit_check == 0 :
    print("0")
    
else:
    print(f"lost is {profit_check}")
