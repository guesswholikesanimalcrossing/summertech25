for i in range(6):
    for k in range (5-i):
     print (" ",end="")
    for j in range(i+1):
     print("* ",end="")
    print()

for i in range(6):
    for k in range (i+1):
     print (" ",end="")
    for j in range(5-i):
     print("* ",end="")
    print()
