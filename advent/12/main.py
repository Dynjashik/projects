file = open("advent/12/new12.txt", "r")

str_list = []
for line in file:
    str_list.append(line)

current_position = ""
right = ">"
left = "<"
up = "^"
down = "v"
for st in str_list:
    print(st)
    for i in range(len(i)):
        if ord(st[i+1])== ord(st[i])+1 or ord(st[i+1])== ord(st[i]):
            st[i] = right
            current_position = st[i+1]
        print(current_position)