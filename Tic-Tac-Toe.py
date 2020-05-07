board = [" " for x in range(10)]

def inputLetter(letter, pos):
    board[pos] = letter
    
def designBoard(board):
    print("   |   |   ")
    print(" "+board[1]+" | "+board[2]+" | " + board[3]+" ")
    print("   |   |   ")
    print("____________")
    print("   |   |   ")
    print(" "+board[4]+" | "+board[5]+" | " + board[6]+" ")
    print("   |   |   ")
    print("____________")
    print("   |   |   ")
    print(" "+board[7]+" | "+board[8]+" | " + board[9]+" ")
    print("   |   |   ")
    
def isFree(pos):
    return board[pos] == " "
    
def isFull(board):
    if board.count(" ") > 1:
        return False
    else:
        return True
    
def isWinner(board,l):
    return ((board[1] == l and board[2] == l and board[3] == l) or
    (board[4] == l and board[5] == l and board[6] == l) or
    (board[7] == l and board[8] == l and board[9] == l) or
    (board[1] == l and board[5] == l and board[9] == l) or
    (board[3] == l and board[5] == l and board[7] == l) or
    (board[1] == l and board[4] == l and board[7] == l) or
    (board[2] == l and board[5] == l and board[8] == l) or
    (board[3] == l and board[6] == l and board[9] == l))
 
def selectRandom(lst):
    import random
    ln = len(lst)
    index = random.randrange(0,ln)
    return lst[index]
    
def playerMove():
    run = True
    while run:
        move = input("Enter the position to place 'x' in between(1,9)")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if isFree(move):
                    run = False
                    inputLetter("x",move)
                else:
                    print("Sorry!! This space is already occupied.Try Another one!")
            else:
                print("Invalid Number enter in between 0 to 9")
        except:
            print("Please enter only Number")
            
def computerMove():
    possible = [x for x, l in enumerate(board) if l == " " and x != 0]
    move = 0
    
    for let in ["o","x"]:
        for i in possible:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy,let):
                move = i
                return move
                
    edgePosition = []
    for i in possible:
        if i in [1,3,7,9]:
            edgePosition.append(i)
    
    if len(edgePosition) > 0:
        move = selectRandom(edgePosition)
        return move
    
    if 5 in possible:
        move = 5
        return move
        
      
    openPosition = []
    
    for i in possible:
        if i in [2,4,6,8]:
            openPosition.append(i)
    
    if len(openPosition) > 0:
        move = selectRandom(openPosition)
        return move
    return move
            
def main():
    print("Welcome To Tic-Tac-Toe")
    designBoard(board)
    
    while not(isFull(board)):
        if not(isWinner(board,"o")):
            playerMove()
            designBoard(board)
        else:
            print("Sorry you lose the game!!")
            break
            
        if not(isWinner(board,"x")):
            move = computerMove() 
            print("computers moves :", move)
            if move == 0:
                print(" ")
                break
            else:
                inputLetter("o",move)
                print("Computer placed 'o' at position : ", move)
                designBoard(board)
        else:
            print("Yeahh you win the game!!")
            break
        
    if isFull(board):
        print("Oops game tie!!")
        
while True:
    
    x = input("Do you want to play the game (y/n) ?")
    if x.lower() == 'y':
        board = [" " for x in range(10)]
        print("-----------------------")
        main()
    else:
        print("Thank You!! We are closing the game.")
        break
        
        
        