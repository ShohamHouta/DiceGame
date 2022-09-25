import logging
from player import Player

pot = 0
player = Player(1000)

logging.basicConfig(filename="log.log")


def menu():
    print("""============================================
===============Dice Rolls===================
============================================

	[i]  Bet on 1 Dice.
	[ii] Bet on Chosen amout of Dices.
	""")


def main():
    global pot

    menu()
    choice = input("Your choice: ")
    try:
        choice = int(choice)
        if choice == 1:
            player.Dice_count(1)
            player.Roll()
        if choice == 2:
            dice_amout = input("Enter the amout of dices to roll: ")
        try:
            dice_amout = int(dice_amout)
            player.Dice_count(dice_amout)
            player.Roll()
        except ValueError as e:
            logging.exception(e)
    except ValueError as e:
        logging.exception(e)


if __name__ == "__main__":
    main()
