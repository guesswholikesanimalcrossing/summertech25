bored=[["_ ","_ ","_ "],["_ ","_ ","_ "],["_ ","_ ","_ "]]
win=False
again=("Y")
mark=("X ")
# for i in bored:
#     print(i)
#     print()
for i in range(0,3):
            for k in range(0,3):
                print(bored[i][k],end="")
            print()
while again==("Y"):
     
    while win==False:
        
        # print("Tic Tac Tie! Nine is Fine! Breakout new Game of the Century by young petty developer Clare at SmarterNotHarder Games.")
        # print("Rules: First to realize how dumb this game is loses, and the other player automatically ties!!!!!! WE ALL LOSE WHEN SOME SEMBLANCE OF SHAPES ARE INVOLVED!!!!")

        row0=int(input("What row would you like to go in? 1, 2, or 3? "))
        row0=row0-1
        column0=int(input("Which column would you like to go in? 1, 2, or 3? "))
        column0=column0-1
        # if row0==0 and column0==0:
        #     bored[0][0]=mark
        #     for i in range(0,3):
        #         for k in range(0,3):
        #             print(bored[i][k],end="")
        #         print()
        while row0>2 or column0>2:
            print("Sorry, this space does not exist.")
            row0=int(input("What row would you like to go in? 1, 2, or 3? "))
            row0=row0-1
            column0=int(input("Which column would you like to go in? 1, 2, or 3? "))
            column0=column0-1
        while bored[row0][column0]!=("_ "):
            print("Sorry, you cannot mark here.")
            row0=int(input("What row would you like to go in? 1, 2, or 3? "))
            row0=row0-1
            column0=int(input("Which column would you like to go in? 1, 2, or 3? "))
            column0=column0-1
             
        bored[row0][column0]=mark
        for i in range(0,3):
                for k in range(0,3):
                    print(bored[i][k],end="")
                print()
        if bored[0][0] == (mark) and bored [0][1] == (mark) and bored[0][2] == (mark):
            print(mark+"wins!")
            win=True
        elif bored[0][0] == (mark) and bored [1][0] == (mark) and bored[2][0] == (mark):
            print(mark+"wins!")
            win=True
        elif bored[1][0] == (mark) and bored [1][1] == (mark) and bored[1][2] == (mark):
            print(mark+"wins!")
            win=True
        elif bored[0][1] == (mark) and bored [1][1] == (mark) and bored[2][1] == (mark):
            print(mark+"wins!")
            win=True
        elif bored[2][0] == (mark) and bored [2][1] == (mark) and bored[2][2] == (mark):
            print(mark+"wins!")
            win=True
        elif bored[0][2] == (mark) and bored [1][2] == (mark) and bored[2][2] == (mark):
            print(mark+"wins!")
            win=True
        elif bored[0][0] == (mark) and bored [1][1] == (mark) and bored[2][2] == (mark):
            print(mark+"wins!")
            win=True
        elif bored[0][2] == (mark) and bored [1][1] == (mark) and bored[2][0] == (mark):
            print(mark+"wins!")
            win=True
        if mark==("X "):
            mark=("O ")
        elif mark==("O "):
            mark=("X ")
    again=input("Play again? Type Y or N. ")
    
    
        

