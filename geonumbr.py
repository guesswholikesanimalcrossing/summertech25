from random import randint
codes=["203","914","401","475","614","215","718","402","917"]
areas=["SW CT","SE NY","RI","SW CT","C OH","SE PA","NYC","E NE","NYC"]
areaCode=(0)
again=("Y")
score=0
while again==("Y"):
    d1=randint(1,9)
    d2=randint(0,9)
    d3=randint(0,9)
    d4=randint(0,9)
    d5=randint(0,9)
    d6=randint(0,9)
    d7=randint(0,9)
    d8=randint(0,9)
    d9=randint(0,9)
    d10=randint(0,9)
    areaCode=(str(d1)+str(d2)+str(d3))
    while areaCode not in codes:
        d1=randint(1,9)
        d2=randint(0,9)
        d3=randint(0,9)
        areaCode=(str(d1)+str(d2)+str(d3))
    print(f"{d1}{d2}{d3}-{d4}{d5}{d6}-{d7}{d8}{d9}{d10}")
    for i in range(len(areas)):
        print((i),areas[i])
    guess=input("Please type the number of the region you think the phone number is from. NE is not New England(not a state btw) ")
    if codes[int(guess)]==areaCode:
        print("good job")
        score=score+1
        again=input("Play again? Type Y or N. ")
        if again==("N"):
           print("Your score was",score)
    elif areaCode==("917") or areaCode==("718"):
        if guess==("6") or guess==("8"):
            print("good job")
            score=score+1
            again=input("Play again? Type Y or N. ")
            if again==("N"):
                print("Your score was",score)
    elif areaCode==("203") or areaCode==("475"):
        if guess==("0") or guess==("4"):
            print("good job")
            again=input("Play again? Type Y or N. ")
            if again==("N"):
                print("Your score was",score)
    else:
        print("sorry, maybe next time!")
        print("Your score was",score)
        again=input("Play again? Type Y or N. ")