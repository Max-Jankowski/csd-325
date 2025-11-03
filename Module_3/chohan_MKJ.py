"""Cho-Han, by Al Sweigart al@inventwithpython.com
The traditional Japanese dice game of even-odd.
View this code athttps://nostarch.com/big-book-small-python-projects
Tags: short, beginner, game

Modifications by: Max Jankowski 
CSD-325 Assignment 3.2
Changes Made:
1. Changed input prompt to initials (mkj:)
2. Changed house fee to collect 12% rather then 10%
3. Added bonus notice in introduction for rolls of 2 or 7
4. Implemented 10 mon bonus for rolls totaling 2 or 7
"""

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

# Change 3: Added a notice to the bonus 10 mon rule
print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.

!!! Bonus: If you roll a total of 2 or 7, you receive a 10 mon bonus! !!!
''')

purse = 5000
while True:  # Main game loop.
    # Place your bet:
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        # First of modification 1: Changed input prompt to initials
        pot = input('mkj: ')  # Changed from '> ' to 'mkj: '
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

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Let the player bet cho or han:
    while True:
        # Second of modification 1: Changed input prompt to initials
        bet = input('mkj: ').upper()  # Changed from '> ' to 'mkj: '
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # Reveal the dice results:
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # Mod 4: Checking for bonuses from 2s or 7s total and award bonus
    diceTotal = dice1 + dice2
    if diceTotal == 2 or diceTotal == 7:
        print()
        print('*** LUCKY ROLL! ***')
        print(f'The dice total is {diceTotal}! You earned a 10 mon bonus!')
        purse = purse + 10  # Add 10 mon bonus to purse
        print()

    # Determine if the player won:
    rollIsEven = (dice1 + dice2) % 2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    # Display the bet results:
    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse = purse + pot  # Add the pot from player's purse.
        # Modification 2- Changed house fee from 10% to 12%
        print('The house collects a', pot * 12 // 100, 'mon fee.')  # Changed from pot // 10
        purse = purse - (pot * 12 // 100)  # the house has incresed its fee to now 12% (changed from 10%)
    else:
        purse = purse - pot  # Subtract the pot from player's purse.
        print('You lost!')

    # Check if the player has run out of money:
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()
