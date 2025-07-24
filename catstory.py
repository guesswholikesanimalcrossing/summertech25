from random import randint
chance=0
again=("Y")
while again==("Y"):
    print("You are a cat. What is your name?")
    name=input("Please enter your name. ")
    print("Hello,",name)
    print("What would you like to do? \na: leave your house\nb: eat some food")
    choice1=input("Please type A or B.")
    if choice1==("A"):
        chance=randint(0,4)
        if chance==0:
            print("Nice try. You got caught by your owner. MEOWWWWW!")
            again=input("Play again? Please input Y or N. ")

        else:
            print("You made it out of the house. What will you do now? \na: make friends with another cat\nb: go back home (why would you do that???)")
            getout=input("Please type A or B.")
            if getout==("A"):
                print("You come across a cat named Barnes. You tell Barnes your name is",name)
                sayToB=input("Please type what you would like to say to Barnes.")
                print(name,"says",sayToB)