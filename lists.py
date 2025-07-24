from random import randint
# # cart=["chocolate","chicken nuggets","iced tea","pepsi","video games"]
# # # yN=("Y")
# # # while yN==("Y"):

itemrandom=randint(0,2)
itemrandom2=randint(0,2)
# # #     print("What should you buy at the store?")
# # #     yN=input("would you like to start? Type Y or N ")
# # #     print(cart[itemrandom])
# # cart.append("Strawberry Candy")
# # cart.remove("pepsi")
# # print(cart)
# # """for i in cart:
# #     print(i)"""

# cart=["juice"]
# again=("Y")
# while again==("Y"):
#     print(cart)
#     print("This is your cart right now.")
#     which=input("Would you like to add or remove an item? Type A or R. ")
#     if which==("A"):
#         add=input("Type the name of an item you would like to add. ")
#         cart.append(add)
#         print(cart)
#         print("This is your cart right now.")
#         again=input("Would you like to modify more? Please type Y or N. ")
#     elif which==("R"):
#         rWhat=input("What would you like to remove? ")
#         if rWhat in cart:
#             cart.remove(rWhat)
#         else:
#             print("The item you requested does not appear to be in the list. Try typing it exactly the way it appears on the list.")
#             print(cart)
#             print("This is your cart right now.")
#             again=input("Would you like to modify more? Please type Y or N. ")

numbers=[[1,2,3],[4,5,6],[7,8,9]]
print(numbers[itemrandom][itemrandom2])