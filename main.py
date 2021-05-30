from backend import *


def displayBoardAs2D():
    print(board[0])
    print(board[1])
    print(board[2])
    print()


# board, rowsContainer, colsContainer, diagonalContainer, oppoDiagonalContainer, player
def init():
    return createboard(), createRowsContainer(), createColsContainer(), createDiagonalContainer(), createOppoDiagonalContainer(), 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # init
    board, rowsContainer, colsContainer, diagonalContainer, oppoDiagonalContainer, player = init()

    # gameflow
    print("Welcome to Tic Tac Toe game")
    while (True):

        print("Player : " + str(player))
        displayBoardAs2D()

        # user input, x is colNum, y is rowNum
        move = input("Please place your move (in format rowNum,colNum) \n")
        rowNum, colNum = move.split(',')

        colNum = int(colNum)
        rowNum = int(rowNum)

        # place userInput into move method

        makeMoke(board, player, colNum, rowNum, rowsContainer, colsContainer, diagonalContainer, oppoDiagonalContainer)

        displayBoardAs2D()

        # next game query

        status = winningVerification(rowsContainer, colsContainer, diagonalContainer, oppoDiagonalContainer)
        if (status):
            if (status == 1):
                print("player X won!")
            if (status == 2):
                print("player O won!")

            nextGameFlag = input("Still want to play? (y/n) : ")
            if (nextGameFlag.lower() != "y"):
                # reset after win, or tie
                break
            board, rowsContainer, colsContainer, diagonalContainer, oppoDiagonalContainer, player = init()
        else:

            # no one win switch player
            player = switchPlayer(player)
