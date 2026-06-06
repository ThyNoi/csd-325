# Eric Sengvanhpheng
# June 6, 2026
# Advanced Python Module 1.3

# Python program that calls a function and loops through a countdown with user input

# Created function for loop and pass input
def countdown(beer_amount):
    while beer_amount > 0:
        if beer_amount == 1:
            print(f"{beer_amount} bottle of beer on the wall, {beer_amount} bottle of beer.")
            beer_amount -= 1
            print(f"Take one down, pass it around, {beer_amount} bottles of beer on the wall.")
            print()

        else:
                print(f"{beer_amount} bottles of beer on the wall, {beer_amount} bottles of beer.")
                beer_amount -= 1
                print(f"Take one down, pass it around, {beer_amount} bottles of beer on the wall.")
                print()

# Get input and make it an int
beer_choice = int(input("How many bottles of beer on the wall? "))

countdown(beer_choice)

print("Out of Beer, buy more beer bottles!")

