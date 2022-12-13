file = open("advent/3/new3.txt", "r")

comp_1 = []
comp_2 = []
letters = []
sum_let = 0
for line in file:
    for a in range(len(line)):
        if a < len(line)//2:
            comp_1.append(line[a])
        else:
            comp_2.append(line[a])
  
    letters.extend(list(set(comp_1).intersection(comp_2)))
    comp_1 = []
    comp_2 = []

print(letters)
for letter in letters:
    if ord(letter)> 96:
        sum_let += ord(letter)-96
    else:
        sum_let += ord(letter)-38
        

print(list(set(comp_1).intersection(comp_2)) )
print(sum_let)