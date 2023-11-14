import time

def glug():
	time.sleep(1)
	print("Glug...")
	time.sleep(1)
	print("Glug...")
	time.sleep(1)
	print("Glug...")
	time.sleep(2)
	print("That was delightful.")
	time.sleep(2)
	
drink_count = 0
	
def offer_drink(drink_type):
	return input(f"Would you like to get a {drink_type}? Yes or no? ").lower()

name = input("Hey there, what's your name? ")
print("Hello,",name)
age = int(input("How old are you? "))

if age >= 21:
	drink_type = "Yuengling"

if age < 21:
	drink_type = "McDonald's™ Sprite™"
	
response = offer_drink(drink_type)

if response == "yes":
		while True:
			print(f"Excellent, let's have an ice cold {drink_type}!")
			glug()
			drink_count += 1
			print(f"Alright, that's {drink_count}. How about another?")
			time.sleep(1)
			
			if offer_drink(drink_type) != "yes":
				break

if response == "no":
	print(f"Okay, I suppose I'll have a quiet {drink_type} by myself. No hard feelings.")
	time.sleep(2)
	print("If you change your mind, let me know!")
	
if drink_count >=1:
	print(f"Alright, I think we've had enough. Between the two of us that was {drink_count * 2}. Let's call it a day.")