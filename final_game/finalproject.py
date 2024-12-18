# Sam Young
# 12/5/24
# COS 121 Final Project
# Choose your own story

def startgame():
    userinput = input("Would you like to play? (yes/no) ").lower().strip()  # asks the user to start the game

    if userinput == "yes":
        cityscene()
    else: 
        print("Thats to bad:(")

def cityscene(): # sets the starting scene of the story
    print("You are walking down the city streets on a sunny afternoon")
    print("You suddenly hear the screech of tires and the breaking of glass")
    print("You look down the street and see that a car has just ran through the front of a jewelry store!")
    
    userinput = input("Do you decide to get a closer look at the action? (yes/no)").lower().strip() # lower and strip makes sure that the anser will work even if it has extra space or capital letters
    
    if userinput == "yes":
        robberyscene()
    else:
        print("Your decide to ignore the accident and you go home")
        print("Later you watch the news to see that you actually witnessed the start of a bank robbery")
        print("You think to youself maybe you should have checked out what was going on")
        print("Your story ends here")
    
def robberyscene(): # stores the narrative in its own specific file
    f = open("robberyscene.txt", "r")
    data = f.read()
    f.close()
    print(data)
        
    userinput = input("Do you try to stop him? (yes/no)").lower().strip()

    if userinput == "yes":
        heropath()
    else:
        cowardpath()

def heropath(): # stores the narrative in its own specific file
    f = open("heropath.txt", "r")
    data = f.read()
    f.close()
    print(data)

    userinput = input("Do you decide to take the bag for yourself or wait until the police arrive? (take/leave)").lower().strip()

    if userinput == "take":
                escapescene()
    else: # stores the narrative in its own specific file
        f = open("easywayout.txt", "r")
        data = f.read()
        f.close()
        print(data)
        
def cowardpath(): # stores the narrative in its own specific file
    f = open("cowardpath.txt", "r")
    data = f.read()
    f.close()
    print(data)

def escapescene(): # stores the narrative in its own specific file
    f = open("escapescene.txt", "r")
    data = f.read()
    f.close()
    print(data)
                
    userinput = input("You come to a light, do you decide to continue driving downtown or get on the highway? (downtown/highway)")

    if userinput == "downtown": # stores the narrative in its own specific file
        f = open("downtown.txt", "r")
        data = f.read()
        f.close()
        print(data)
    
    else: # stores the narrative in its own specific file
        f = open("highwayscene.txt", "r")
        data = f.read()
        f.close()
        print(data)


startgame() # finishes up the game ending the loop





