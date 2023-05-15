miles_traveled = 0
thirst = 0
camel_tiredness = 0
natives_distance = -20
drinks = 3
player_pos = 0
natives_pos = 0
loser = True


print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down! Survive your")
print("desert trek and out run the natives.")

done = False

while not done:
    random_oasis = 0
    print("\nA. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")

    user_choice = input("What is your choice? ")

    if user_choice.upper() == "Q":
        print("Aww you quit :(")
        done = True

    elif user_choice.upper() == "A":
        # DRINK FROM CANTEEN
        print("A")

    elif user_choice.upper() == "B":
        # AHEAD MODERATE SPEED
        print("B")

    elif user_choice.upper() == "C":
        # AHEAD FULL SPEED
        print("C")

    elif user_choice.upper() == "D":
        # STOP FOR THE NIGHT
        print("D")

    elif user_choice.upper() == "E":
        # STATUS CHECK
        print("\nMiles traveled:", miles_traveled)
        print("Drink in canteen:", drinks)
        print("The natives are", miles_traveled - natives_distance, "miles behind you")
