import random

def hangman():
    word = random.choice(["peach", "banana", "apple", "grapes", "strawberry", "pineapple", "raspberry"])
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turn = 10
    guessMade = ""
    while turn > 0:
        show = ""
        compare = ""
        for i in word:
            if i in guessMade:
                show = show + i + " "
                compare += i
            else:
                show += "_ "

        print("Word to be guessed : ", show)
        if compare != word:
            print("guessword", guessMade)
            guess = input("Guess a letter : ")
            if guess in validLetters:
                if guess in word:
                    print("Yeah !! you guessed right letter..")
                    guessMade += guess
                else:
                    turn -= 1
                    print("Oops !! you guessed wrong letter..")
                    if turn != 0:
                        print("You have only ",turn," turns left")
                        print("==============================")
                        printMan(turn)
                        print("==============================")
                    else:
                        print("Sorry!! You lose the game..")
                        print("==============================")
                        printMan(turn)
                        print("==============================")
                        print("HANGMAN DIED!!")
                        break
            else:
                print("Enter valid letter..")
        else:
            print("Yeah!! you guessed the whole word correctly :-)")
            
            break
            
def printMan(turn):
    if turn == 9:
        print('')
        print('          O ')
        print('')
    if turn == 8:
        print('')
        print('          O  ')
        print('          |  ')
        print('')
    if turn == 7:
        print('')
        print('          O  ')
        print('         /|  ')
        print('')
    if turn == 6:
        print('')
        print('          O  ')
        print('         /|\ ')
        print('')
    if turn == 5:
        print('')
        print('          O  ')
        print('         /|\ ')
        print('          |  ')
        print('')
    if turn == 4:
        print('')
        print('          O  ')
        print('         /|\ ')
        print('          |  ')
        print('         /   ')
        print('')
    if turn == 3:
        print('')
        print('          O  ')
        print('         /|\ ')
        print('          |  ')
        print('         / \ ')
        print('')
    if turn == 2:
        print('')
        print('          O | ')
        print('         /|\ ')
        print('          |  ')
        print('         / \ ')
        print('')
    if turn == 1:
        print('')
        print('          O _| ')
        print('         /|\ ')
        print('          |  ')
        print('         / \ ')
        print('')
    if turn == 0:
        print('')
        print('          O_| ')
        print('         /|\ ')
        print('          |  ')
        print('         / \ ')
        print('')


name = input('Enter your name : ')
print("Welcome!! %s to the Hangman Game" %name)
print("Try to guess the word in less than 10 attempts..")
print('=====================================')
hangman()



