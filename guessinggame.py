from random import randint;

randomNumber =randint(1,100)

print("Time to guess!")
guessCount=0
guess=-1

while(True and guessCount<7):
    guess=int(input("Please input a number between 1 and 100. "))
    guessCount+=1
    if guess==randomNumber:
        print("You Guessed It!!!!!!!!!!!!!!!")
        break
    elif guess>randomNumber:
        print("The number is LOWER than what you guessed.")
    elif guess<randomNumber:
        print("The number is HIGHER than what you guessed.")
if guessCount==7 and guess!=randomNumber:
    print("Too bad. Ya ran out of guesses LOLLOOOOOLLL")