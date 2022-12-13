file = open("advent/2/new2.txt", "r")

my_score = 0
opp_score = 0
for line in file:
  if line[0] == "A" and line[2]=="X":
      my_score += 4
      opp_score += 4

  if line[0] == "B" and line[2]=="Y":
      my_score+= 5
      opp_score+= 5
  
  if line[0] == "C" and line[2]=="Z":
      my_score+= 6
      opp_score+= 6

  if line[0] == "A" and line[2]=="Y":
      my_score += 8
      opp_score +=1

  if line[0] == "A" and line[2]=="Z":
      my_score += 3
      opp_score += 7

  if line[0] == "B" and line[2]=="Z":
      my_score += 9
      opp_score += 2

  if line[0] == "B" and line[2]=="X":
      my_score += 1
      opp_score += 8

  if line[0] == "C" and line[2]=="X":
      my_score += 7
      opp_score += 3

  if line[0] == "C" and line[2]=="Y":
      my_score += 2
      opp_score += 9

    
print(my_score)






    
