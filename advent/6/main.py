file = open("advent/6/new6.txt", "r")

list_1 = []
count_marker = 0
for line in file:
    for a in line:
        print("READING " + a)
        if len(list_1) == 4:
            set_1 = set(list_1)
            print("list: " + str(list_1))
            print("set: " + str(set_1))
            
            if len(list_1) == len(set_1):
                print("They are the same! count marker="+str(count_marker))
                break
            else:
                list_1.pop(0)
                print("List after pop" + str(list_1))
                list_1.append(a)
                count_marker += 1
        else:
            list_1.append(a)
            print("appended to list: " + a)


print(len(list_1)+count_marker)

  


