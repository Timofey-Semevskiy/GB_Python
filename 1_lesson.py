seconds_input = int(input("Enter your number: "))
hours = 0
seconds = 0
minuts = 0

if seconds_input > 60:
    minuts = seconds_input // 60
    seconds = seconds_input % 60

if minuts > 60:
    hours = minuts // 60
    minuts = minuts % 60

print(f"hours: {hours}, minuts: {minuts} ,seconds: {seconds}")
