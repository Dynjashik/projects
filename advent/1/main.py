file = open("advent/1/input.txt", "r")

max_cal = 0
max_current = 0
for line in file:
    if line != "\n":
        max_current+= int(line)
    else:
        if max_current > max_cal:
            max_cal= max_current
        max_current = 0

print(max_cal)





    
