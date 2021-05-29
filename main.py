from backend import *


def displayBoardAs2D():
    print(board[0])
    print(board[1])
    print(board[2])
    print()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    board = createboard()
    rowsContainer = createRowsContainer()
    colsContainer = createColsContainer()
    diagonalContainer = createDiagonalContainer()
    oppoDiagonalContainer = createOppoDiagonalContainer()

    displayBoardAs2D()
    board = makeMoke(board, 2, 0, 0, rowsContainer, colsContainer, diagonalContainer, oppoDiagonalContainer)
    print(winningVerification(rowsContainer, colsContainer, diagonalContainer, oppoDiagonalContainer))
    displayBoardAs2D()

    board = makeMoke(board, 2, 1, 1, rowsContainer, colsContainer, diagonalContainer, oppoDiagonalContainer)
    print(winningVerification(rowsContainer, colsContainer, diagonalContainer, oppoDiagonalContainer))
    displayBoardAs2D()

    board = makeMoke(board, 2, 2, 2, rowsContainer, colsContainer, diagonalContainer, oppoDiagonalContainer)
    print(winningVerification(rowsContainer, colsContainer, diagonalContainer, oppoDiagonalContainer))
    displayBoardAs2D()

    print(diagonalContainer)
