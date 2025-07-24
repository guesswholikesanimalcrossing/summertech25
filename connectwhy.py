bored=[]
win=False
mark=("X ")
for j in range(0,6):
    bored.append(["_ ","_ ","_ ","_ ","_ ","_ ","_ "])
for i in range(0,6):
            for k in range(0,7):
                print(bored[i][k],end="")
            print()
while win==False:

      column0=int(input("Which column would you like to go in? 1, 2, 3, 4, 5, 6, or 7? "))
      column0=column0-1
      if bored[5][column0]==("_ "):
            bored[5][column0]=mark
      elif bored[4][column0]==("_ "):
            bored[4][column0]=mark
      elif bored[3][column0]==("_ "):
            bored[3][column0]=mark
      elif bored[2][column0]==("_ "):
            bored[2][column0]=mark
      elif bored[1][column0]==("_ "):
            bored[1][column0]=mark
      elif bored[0][column0]==("_ "):
            bored[0][column0]=mark
      for i in range(0,6):
                  for k in range(0,7):
                        print(bored[i][k],end="")
                  print()
      for i in range(6):
             for j in range(3):
                  if bored

      if mark==("X "):
            mark=("O ")
      elif mark==("O "):
            mark=("X ")                                                                                                                                                                                         