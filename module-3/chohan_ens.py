"""Cho-Han, by Al Sweigart al@inventwithpython.com
The traditional Japanese dice game of even-odd.
View this code athttps://nostarch.com/big-book-small-python-projects
Tags: short, beginner, game"""

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.
*If you get a 2 or a 7 total on a dice roll, you get a 10 mon bonus!*''')

purse = 5000
while True:  # Main game loop.
    # Place your bet:
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        pot = input('ens: ') 
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            # This is a valid bet.
            pot = int(pot)  # Convert pot to an integer.
            break  # Exit the loop once a valid bet is placed.

    # Roll the dice.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    # Dice roll total 
    dice_total = dice1 + dice2

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Let the player bet cho or han:
    while True:
        bet = input('ens: ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # Reveal the dice results:
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)
    print(f'Dice total: {dice_total}')

    # Determine if the player won:
    rollIsEven = dice_total % 2 == 0 # Replace is dice total variable
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    # Calculate house fee
    fee = pot * 12 // 100

    # Display the bet results:
    if playerWon:
        if dice_total == 2 or dice_total ==7: 
            print(f'You won! Your dice total was {dice_total}. You receive a 10 mon bonus and take {pot} mon.') 
            purse = purse + 10 # Add mon bonus
            purse = purse + pot  # Add the pot from player's purse.
            print('The house collects a', fee, 'mon fee.')
            purse = purse - fee  # The house fee is 12%.
        else:    
            print('You won! You take', pot, 'mon.')
            purse = purse + pot  # Add the pot from player's purse.
            print('The house collects a', fee, 'mon fee.')
            purse = purse - fee  # The house fee is 12%.
    else:
        if dice_total == 2 or dice_total ==7:
            print(f'You lost, but your dice total was {dice_total}. You receive a 10 mon bonus.') 
            purse = purse + 10 # Add mon bonus
            purse = purse - pot 
        else: 
            # Subtract the pot from player's purse.
            print('You lost!')
            purse = purse - pot

    # Check if the player has run out of money:
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()
