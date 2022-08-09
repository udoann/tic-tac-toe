# ticTactoeNon_oop.py A  non -OOP tic-tac-toe game.

ALL_SPACES = list('123456789')
X, O, BLANK ='X', 'O', ' ' # Constants for string values.

def main():
    """Runs a game of tic-tac-toe."""
    print('Welcome to tic-tac-toe!')
    gameBoard = getBlankBoard()  # Create a TTT board dictionary.
    currentPlayer, nextPlayer = X, O  # X goes first, O goes next.
    
    while True:
        print(getBoardStr(gameBoard))  # Display the board on the Screen.

        # Keep asking the player untill they enter a number 1-9:
        move = None
        while not isValidSpace(gameBoard, move):
            print(f'What is {currentPlayer}\'s move? (1-9)')
            move = input()
        updateBoard(gameBoard, move, currentPlayer)  # MAke tge move.

        # Check if the game is over:
        if isWinner(gameBoard, currentPlayer):  # First check for victory.
            print(getBoardStr(gameBoard))
            print(currentPlayer + ' has won the game!')
            break
        elif isBoardFull(gameBoard):  # next check for a tie.
            print(getBoardStr(gameBoard))
            print('The game is a tie!')
            break
        currentPlayer, nextPlayer = nextPlayer, currentPlayer  # Swap turns.
    print('Thanks for Playing')

def getBlankBoard():
    """Create a new, blank tic-tac-toe board"""
    board = {}
    for space in ALL_SPACES:
        board[space] = BLANK  # All spac start as blank.
    return board
def getBoardStr(board):
    """Returns a text representation of the board."""
    return f'''
        {board['1']}|{board['2']}|{board['3']} 1 2 3 
        -+-+-
        {board['4']}|{board['5']}|{board['6']} 4 5 6 
        -+-+-
        {board['7']}|{board['8']}|{board['9']} 7 8 9'''
def isValidSpace(board, space):
    """Returns True if the space on the board is a valid space number
    and the space is balnk"""
    return space in ALL_SPACES or board[space] == BLANK
def isWinner(board, player):
    """Return True if player ids a winner on this TTT board."""
    b,p = board, player
    # Check for 3 marks across the 3 rows, 3 columns, and 2 diagoanals.
    return((b['1'] == b['2'] == b['3'] == p)or # Across the top
           (b['4'] == b['5'] == b['6'] == p)or # Across the middle
           (b['7'] == b['8'] == b['9'] == p)or # Across the bottom
           (b['1'] == b['4'] == b['7'] == p)or # Down the left
           (b['2'] == b['5'] == b['8'] == p)or # Down the middle
           (b['3'] == b['6'] == b['9'] == p)or # Down the right
           (b['3'] == b['5'] == b['7'] == p)or # Diagonal
           (b['1'] == b['5'] == b['9'] == p))  # Diagonal
def isBoardFull(board):
    """Return True if every space on the board has been taken."""
    for space in ALL_SPACES:
        if board[space] == BLANK:
            return False
    return True  # No spaces ARE BLANK, so return True.

def updateBoard(board, space , mark):
    """Sets the space on the board to mark"""
    board[space] = mark

if __name__ == '__main__':
    main()  # Call main() if this mpodule is run, but not when imported.