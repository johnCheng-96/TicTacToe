import array as arr

#   012
# 0 123
# 1 456
# 2 789


# size 9 array, 0 means null, 1 means x, 2 means o
# x play first
import math


def createboard():
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    return board


def createRowsContainer():
    return [0, 0, 0]


def createColsContainer():
    return [0, 0, 0]


def createDiagonalContainer():
    return [0]


def createOppoDiagonalContainer():
    return [0]


def makeMoke(board, who, x, y, rowsCon, colsCon, diaCon, oppCon):
    if (who == 0):
        return board

    # visualisation
    board[y][x] = who

    # container

    # rows
    rowsCon[y] += who

    # cols
    colsCon[x] += who

    # dia
    if x == y:
        diaCon[0] += who

    # oppoDia
    if (abs(y - x) == 2 or x == y == 1):
        oppCon[0] += who

    return board


# Verify winning status after each play

# O(n)
def rowWinningVerification(rowsContainer):
    for n in rowsContainer:
        if (n == 3):
            return 1
        if (n == 6):
            return 2

    return 0


# O(n)
def colWinningVerification(colsContainer):
    for n in colsContainer:
        if (n == 3):
            return 1
        if (n == 6):
            return 2

    return 0


# O(1)
def diagonalWinningVerification(diagonalContainer):
    if diagonalContainer[0] == 3:
        return 1
    if diagonalContainer[0] == 6:
        return 2

    return 0


# O(1)
def oppoDiagonalWinningVerification(oppoDiagonalContainer):
    if oppoDiagonalContainer[0] == 3:
        return 1
    if oppoDiagonalContainer[0] == 6:
        return 2

    return 0


def winningVerification(rowsContainer, colsContainer, diagonalContainer, oppoDiagonalContainer):
    if verdict := rowWinningVerification(rowsContainer):
        return verdict

    if verdict := colWinningVerification(colsContainer):
        return verdict
    if verdict := diagonalWinningVerification(diagonalContainer):
        return verdict
    if verdict := oppoDiagonalWinningVerification(oppoDiagonalContainer):
        return verdict

    return 0
