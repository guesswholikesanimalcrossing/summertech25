from random import randint
import pygame
pygame.init()
fr=open("highscore.txt","r")
codes=["907", "205", "479", "480", "209", "303", "203", "202", "302", "239",
    "229", "808", "319", "208", "217", "812", "316", "270", "225", "413",
    "301", "207", "231", "218", "314", "662", "406", "252", "308", "701", "603",
    "201", "505", "702", "917", "614", "405", "503", "215", "401", "803",
    "605", "423", "210", "435", "276", "802", "206", "262", "304", "307"]
areas=["Alaska", "Alabama", "Arkansas", "Arizona", "California", "Colorado",
    "Connecticut", "District of Columbia", "Delaware", "Florida", "Georgia",
    "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky",
    "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan",
    "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina",
    "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico",
    "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
    "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas",
    "Utah", "Virginia", "Vermont", "Washington", "Wisconsin", "West Virginia",
    "Wyoming"]
areaCode=(0)
again=("Y")

score=0
while again==("Y"):
    print("Welcome to Geonumbr: The Final Form")
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
    guess=input("Please type the number of the region you think the phone number is from. ")
    if codes[int(guess)]==areaCode:
        print("good job")
        score=score+1
    else:
        print("tough, man. you got it wrong. you REALLY need to brush up on those facts of yours.")
    again=input("Play again? Type Y or N. ")
    if again==("N"):
    #    print(fr.readable())
        print("Your score was",score)
        if score>int(fr.read()):
            fr.close()
            f=open("highscore.txt","w")
            f.write (str(score))
            print("NEW HIGH SCORE!!!!! YOUR SCORE WAS HIGH, AND IT WAS",score)
            f.close()

        else:
            fr=open("highscore.txt","r")
            print("Your score was",score)
            print("The current high score is",int(fr.read()))
fr.close()