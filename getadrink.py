name = input("What is your name? ")
print("Hello,", name)
age = int(input("How old are you? "))
if age >= 21:
    choice = input("Would you like to get a beer? Yes or no? ")
    if choice.lower() == "yes":
        print("Alright, let's have a drink!")
    else:
        print("Okay, I won't take it personally.")
else:
    choice = input("Would you like to get a soda? Yes or no? ")
    if choice.lower() == "yes":
        print("Alright, let's get some McDonald's Sprite!")
    else:
        print("Okay, I'll have some Sprite by my lonesome.")
