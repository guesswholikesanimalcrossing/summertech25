from random import randint
friends=randint(0,3)
inventory=[]
gasagain=("Y")
moneyrandom=randint(0,10000)
print("you have",moneyrandom,"money.")
print("You have",friends,"friend(s).")
if friends==0:
    print("Like a true coder!!!!!!")
nuggetsyesno=input("Would you like to buy chicken nuggets? Type Y or N. ")
if nuggetsyesno==("Y") and moneyrandom>=10:
    moneyrandom=moneyrandom-10
    print("you have",moneyrandom,"money.")
    print("You have purchased Chicken nuggets")
    inventory.append("Chicken Nuggets")
    print("inventory check: You have",inventory)
elif nuggetsyesno==("Y") and moneyrandom<10:
    print("Nah you broke lol, you have",moneyrandom,"money.")
elif nuggetsyesno==("N"):
    print("Really? LOL bro chicken is so yum idk what ur on about")

print("A person approaches you. They say, Can I have some chicken nuggets? ")
if nuggetsyesno==("N"):
    print("You are sad because you have no chicken nuggets to offer.")
elif nuggetsyesno==("Y"):
    print("You say, Sure! You give them 3 of your nuggets.")
    print("Acquired +1 friend!")
    friends=friends+1
    print("You now have",friends,"friend(s).")
print("You spot a gas station on the horizon. You head in.")
while gasagain==("Y"):
    gasbuy=["oreos","soda can","gas","energy drink"]
    gasbuyprices=[5,3,15,5]
    print("You see many things. What do you buy?")
    for i in range(len(gasbuy)):
        print((i),gasbuy[i])
    buyatstation=int(input("Please type the number of the thing you would like to buy. "))
    for i, thing in enumerate(gasbuy):
        if gasbuy[buyatstation]==thing:
            if moneyrandom<gasbuyprices[buyatstation]:
                print("no money for that stuff... try restarting the game...")
            else:
                moneyrandom=moneyrandom-gasbuyprices[i]
                print("You have",moneyrandom,"money.")
                print("You have purchased",gasbuy[buyatstation])
                inventory.append(gasbuy[buyatstation])
                print("inventory check: You have",inventory)
                gasagain=input("Would you like to buy more? Please type Y or N.")
print("You walk out of the gas station. There is a flame there, crying.")
whatswrongfire=input("Ask what's wrong? Type Y or N.")
if whatswrongfire==("Y"):
    print("The flame says, 'I'm hungry and I don't have any food to help me grow strong. I need gas...'")