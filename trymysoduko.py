sodugrid =  [[0,0,0,0,0,0,0,5,0],
             [0,0,8,3,0,0,0,0,1],
             [3,0,0,4,2,5,0,6,0],
             [7,8,5,0,0,3,0,0,4],
             [6,0,0,0,4,0,0,0,9],
             [4,0,0,2,0,0,8,3,6],
             [0,3,0,5,6,8,0,0,2],
             [5,0,0,0,0,4,7,0,0],
             [0,9,0,0,0,0,0,0,0]]



def printsodokub(brd):
    for i in range(len(brd)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(len(brd[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(brd[i][j])
            else:
                print(str(brd[i][j]) + ' ', end='')
def isemp(brd):
    for i in range(len(brd)):
        for j in range(len(brd[0])):
            if brd[i][j] == 0:
                return (i,j)
    return None
def validbrd(board, num, row, col):
    for i in range(len(board[0])):
        if board[row][i] == num and col != i:
            return False
    for j in range(len(board)):
        if board[j][col] == num and row != j:
            return False
    box_X = col // 3
    box_y = row // 3
    for i in range(box_X*3, box_y*3 +3):
        for j in range(box_y*3, box_X*3 +3):
            if board[i][j] == num and (row,col) != (i,j) :
                return False
    return True
def solution(board):
    empty = isemp(board)
    if empty:
       row,col = empty
    else:
        return True
    for i in range(1,10):
        if validbrd(board, i, row, col):
            board[row][col] = i 
            if solution(board):
                return True
            board[row][col] = 0
    return False

solution(sodugrid)
printsodokub(sodugrid)
