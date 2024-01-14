list = [1,2,3,4,5,6,7,8]

for i in range(0,len(list)-1,2):
    list[i], list[i+1] = list[i+1], list[i]
    


print(list)