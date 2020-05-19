print("""You enter a dark room with two doors.
Do you go through door #1, door #2 or door #3?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's rettina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

elif door == "3":
    print("You are welcome to the new level")
    print("1. Danger zone")
    print("2. Cool zone")

    zone = int(input("> "))
    if zone == 1:
        print("Are you sure you want to come here?")
        certain = input("> ")
        if certain == "Yes":
            print("You are welcome to the battle zone. Get ready to rambo!")
        elif certain == "No":
            print("I never knew you were such a coward. You're a loser!")
        else:
            print("You can still try latter.")
    elif zone == 2:
        print("You are welcome to the land of peace.")
        print("Where would you like to go again from here?")
        print("1. Go to wonder land.")
        print("2. Go to love city.")

        choice = int(input("> "))

        if choice == 1:
            print("You are welcome to wonderland where everythig looks wonderful.")
        elif choice == 2:
            print("This is love city. Enjoy your stay with us.")
        else:
            print(f"Please you've decided to enter {choice} thank you for playing.")

else:
    print("You stumbled around and fall on a knife and die. Good job!")
