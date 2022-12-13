28-47,45-47
file = open("advent/4/new4.txt", "r")

list_0, list_1, list_2 = [],[],[]
a = 0
for line in file:
    list_0 = line.split(",")
    list_1 = list_0[0].split("-")
    list_2 = list_0[1].split("-")

    list_1 = list(range(int(list_1[0]), int(list_1[1])+1))
    list_2 = list(range(int(list_2[0]), int(list_2[1])+1))

    if set(list_1).issubset(list_2) or set(list_2).issubset(list_1):
        a += 1
        



  
print(a)






    
