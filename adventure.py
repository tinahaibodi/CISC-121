def resroom():
    print("You are now in your room. You have have 3 options. On top of that you will always have the chance to check your inventory and the amount of flex dollars you have. \n", "E to exit the room\n", "S to sleep and end the game\n", "N to get dressed up\n", "F for flex dollars\n", "I for inventory\n)
    action = input("What do you want to do?: ")
    if action == "E" or action == "e":
        hallway()
    elif action == "S" or "s":
        print("Goodbye")
        quit()
    elif action == "N" or "n":
        hallway()
def hallway():
    print("You are now in the hallway. What do you want to do?", "F to go to Forrest's room\n", "J to go to Jack's room\n", "E to exit the building\n")
    action = input("Where do you want to go?: ")
    if action == "F" or action == "f":
        forrest()
    elif action == "J" or action == "j":
        jack()
    elif action == "E" or "e":
        food()
def forrest():
    print("You enter forrest's room. He is working on his assignment")
    action = input("Say hello: ")
    if action == "hello" or action == "hey":
        print("Hey man, I'm kinda busy right now, I'll talk to you later")
        hallway()
def jack():
    print("you enter Jack's room. He is watching Netflix")
    print("Hey man, wanna go out for breakfast?")
    action = input("you have two options. Y or N: ")
    if action == "y" or action == "Y":
        print("Okay let's go now")
        food()
    elif action == "n" or action == "N":
        print("Nah man, I have to do something else")
        hallway()
def food():
    print("You are now outside. You have 3 options for food.\n", "Lazy\n", "Lenny\n", "Loco\n")
    action = input("Where do you want to go?: ")
    if action == "Lazy" or action == "lazy":
        lazy()
    elif action == "Lenny" or "lenny":
        lenny()
    elif action == "Loco" or "loco":
        loco()
def lazy():
    print("You are now in lazy. You have 3 options", "p for pasta\n", "f for a four piece\n", "s for a sandwich\n")
    action = input("what do you want to eat?: ")
    if action == "p" or action == "P":
        print("You have gotten pasta.")
        inventory.append("Pasta")
    elif action == "f" or "F":
        print("You have gotten a four piece.")
        inventory.append("Four piece")
    elif action == "s" or "S":
        print("You have gotten a sandwich")
        inventory.append("sandwich")
    action2 = input("You have gotten food. Do you want to eat here or back in your res room? (r for res, h for here: ")
    if action2 == "r" or action == "R":
        print("You eat over here")
        resroom()
    elif action2 == "h" or "H":
        print("While walking back to your res, you failed to look both ways before crossing the street. Unfortunately, a speeding car hit you at max speed. You are dead. The famous slogan you once heard during frosh week 'cars kill frosh' is now a reality. RIP")
        print("Goodbye fellow student. Hope you enjoyed your time at Queen's University")
        quit()
def lenny():
    print("You are now in lenny. You have 4 options\n", "p for pasta\n", "b for burger\n", "s for stirfry\n", "a for all")
    action = input("what do you want to eat?: ")
    if action == "p" or action == "P":
        print("You have gotten pasta.")
        inventory.append("pasta")
    elif action == "b" or action == "B":
        print("You have gotten a burger.")
        inventory.append("burger")
    elif action == "s" or action == "S":
        print("You have gotten stirfry")
        inventory.append("stirfry")
    elif action == "a" or action == "A":
        print("You have gotten everything")
        inventory.append("pasta")
        inventory.append("burger")
        inventory.append("stirfry")
        print("You now have", inventory)
        resroom()

def loco():
    print("You are now in loco. You have 3 options\n", "b for burger\n", "f for four piece\n", "d for dessert")
    action = input("what do you want to eat?: ")
    if action == "d" or action == "D":
        print("You have gotten dessert.")
        inventory.append("dessert")
    elif action == "b" or action == "B":
        print("You have gotten a burger.")
        inventory.append("burger")
    elif action == "f" or action == "F":
        print("You have gotten four piece")
        inventory.append("four piece")
    print("You now have", inventory)
    resroom()
    
    
    
inventory = []
money = 50
print("Welcome to the most realistic Queen's University simulator, you will be role-playing a hungover student on a saturday morning. You will have the options of visiting your floormates, getting some food to quench that hunger and sleeping. The game starts with you waking up at 11:00AM in your bed in McNeill House.")
resroom()
