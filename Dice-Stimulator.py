import random
def printDice(dice):
    if dice == 1:
        print(" ------- ")
        print("|       |")
        print("|   0   |")
        print("|       |")
        print(" ------- ")
    
    if dice == 2:
        print(" ------- ")
        print("| 0     |")
        print("|       |")
        print("|     0 |")
        print(" ------- ")

    if dice == 3:
        print(" ------- ")
        print("| 0     |")
        print("|   0   |")
        print("|     0 |")
        print(" ------- ")

    if dice == 4:
        print(" ------- ")
        print("| 0   0 |")
        print("|       |")
        print("| 0   0 |")
        print(" ------- ")

    if dice == 5:
        print(" ------- ")
        print("| 0   0 |")
        print("|   0   |")
        print("| 0   0 |")
        print(" ------- ")

    if dice == 6:
        print(" ------- ")
        print("| 0 0 0 |")
        print("| 0 0 0 |")
        print("| 0 0 0 |")
        print(" ------- ")
        

while True:
    game = input("Do you want to roll the Dice (y/n) ?")

    if game.lower() == 'y':
        dice = random.randrange(1,7)
        printDice(dice)
    else:
        print('Thank You!! We are closing the game.')
        break