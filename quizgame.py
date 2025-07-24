score=0
print("Welcome to Quiz Central. Please enter a player name.")
name=input("What's your name???")
print("Hello,",name)
print("First question: The original Animal Crossing was released in North America in which year?")
print("a:2001\n"+ "b:2008\n"+ "c:2002\n"+ "d:2005")
q1=input("Please write your answer in lowercase as the letter.")
if q1==("c"):
    print("Correct! Increasing your score by 100 points...")
    score=score+100
else:
    print("Wrong! The original Animal Crossing released in 2002 in North America. Your score is",score)
print("Next up: more gaming. What was the name of the creator of Minecraft?")
print("a:Jeb Borgenson\n"+"b:Markus Persson\n"+"c:Steve\n"+"d:No one, Minecraft just popped into existence idk")
q2=input("Please write your answer in lowercase as the letter.")
if q2==("b"):
    print("Nice job! Score going up...")
    score=score+100
    print("Your score is now",score)
elif q2==("d"):
    print("Dude, game devs exist?????? By the way, your score is",score)
else:
    print("Nope! His name is Markus Perssonm, AKA Notch! your score is",score)
print("LAST ONE!!!!! Did you like my quiz?")
q3=input("Please input Y or N")
if q3==("Y"):
    print("Yay, thanks! You'll get a big boost for that!!!")
    score=score+500
    print("Your score is now",score)
else:
    print("Aww man!!! I hope you realise how cool it is soon!")
    print("Your final score was",score)