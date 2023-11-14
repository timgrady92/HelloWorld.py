import time

name = input("What is your name? ")
print("Hello,", name)
age = int(input("How old are you? "))
if age >= 21:
    choice = input("Would you like to get a beer? Yes or no? ")
    if choice.lower() == "yes":
        print("Alright, let's have a drink!")
        time.sleep(1)
        print("Glug...")
        time.sleep(1)
        print("Glug...")
        time.sleep(1)
        print("Glug...")
        time.sleep(2)
        print("That was delightful.")
    else:
        print("Okay, I won't take it personally.")
else:
    choice = input("Would you like to get a soda? Yes or no? ")
    if choice.lower() == "yes":
        print("Alright, let's get some McDonald's Sprite!")
        time.sleep(1)
        print("Glug...")
        time.sleep(1)
        print("Glug...")
        time.sleep(1)
        print("Glug...")
        time.sleep(2)
        print("That was delightful.")
    else:
        print("Okay, I'll have some Sprite by my lonesome.")
        
time.sleep(2)

print("Back at it. See you next time.")
