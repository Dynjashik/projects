list_1 = ["Q", "M", "G", "C", "L"]
list_2 = ["R", "D", "L", "C", "T", "F", "H", "G"]
list_3 = ["V", "J", "F", "N", "M", "T", "W", "R"]
list_4 = ["J", "F", "D", "V", "Q", "P"]
list_5 = ["N", "F", "M", "S", "L", "B", "T"]
list_6 = ["R", "N", "V", "H", "C", "D", "P"]
list_7 = ["H", "C", "T"]
list_8 = ["G", "S", "J", "V", "Z", "N", "H", "P"]
list_9 = ["Z", "F", "H", "G"]

file = open("advent/5/new5.txt", "r")
list_move = []
for line in file:
    list_move = line.split(" ")
    list_move[-1] = list_move[-1].replace("\n", "")
    print(list_move)

    if list_move[3] == "1":
        from_list = list_1
    if list_move[3] == "2":
        from_list = list_2
    if list_move[3] == "3":
        from_list = list_3
    if list_move[3] == "4":
        from_list = list_4
    if list_move[3] == "5":
        from_list = list_5
    if list_move[3] == "6":
        from_list = list_6
    if list_move[3] == "7":
        from_list = list_7
    if list_move[3] == "8":
        from_list = list_8
    if list_move[3] == "9":
        from_list = list_9

    if list_move[5] == "1":
        to_list = list_1
    if list_move[5] == "2":
        to_list = list_2
    if list_move[5] == "3":
        to_list = list_3
    if list_move[5] == "4":
        to_list = list_4
    if list_move[5] == "5":
        to_list = list_5
    if list_move[5] == "6":
        to_list = list_6
    if list_move[5] == "7":
        to_list = list_7
    if list_move[5] == "8":
        to_list = list_8
    if list_move[5] == "9":
        to_list = list_9
    

    letter = ""    
    for i in range(0, int(list_move[1])):
        letter = from_list.pop()
        to_list.append(letter)  
    

print(list_1[-1],list_2[-1],list_3[-1],list_4[-1],list_5[-1],
      list_6[-1],list_7[-1],list_8[-1],list_9[-1])



