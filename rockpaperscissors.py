from random import randint 
again=("Y")
while again==("Y"): 
    compChoice= randint(0,2)
    userChoice=input("What would you like to pick? Rock, paper, or scissors? (Please enter a capital letter[R, P, or S])")
    if userChoice==("R") and compChoice==0:
        print("You tied!")
    elif userChoice==("R") and compChoice==1:
        print("You lost. Paper covers rock.")
    elif userChoice==("R") and compChoice==2:
        print("You won! Rock smashes scissors!")
    elif userChoice==("P") and compChoice==0:
        print("You won! Paper covers rock!")
    elif userChoice==("P") and compChoice==1:
        print("You tied!")
    elif userChoice==("P") and compChoice==2:
        print("You lost. Scissors cut paper.")
    elif userChoice==("S") and compChoice==0:
        print("You lost. Rock smashes scissors.")
    elif userChoice==("S") and compChoice==1:
        print("You won! Scissors cut paper!")
    elif userChoice==("S") and compChoice==2:
        print ("You tied!")
    again=input("Would you like to play again? Type Y or N ")


