# Eric Sengvanhpheng
# June 6, 2026
# Advanced Python Module 1.3

# Python program that calls a function and loops through a countdown

# Ask the user how many bottles of beer are on the wall.
# Pass that input to a function that manages the countdown.
# The function should take the input and count backwards to 1
# while displaying the number of remaining bottles of beer on the wall.
# Once the count is down to 1, change lyrics to show "1 bottle of beer..."
# At the end of the countdown, get back to the main program and remind the user to buy more beer.

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

