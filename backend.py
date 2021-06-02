import array as arr


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

    # avoid winning collsion
    if (who == 2):
        who *= 2
    # containers
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
        if (n == 12):
            return 2

    return 0


# O(n)
def colWinningVerification(colsContainer):
    for n in colsContainer:
        if (n == 3):
            return 1
        if (n == 12):
            return 2

    return 0


# O(1)
def diagonalWinningVerification(diagonalContainer):
    if diagonalContainer[0] == 3:
        return 1
    if diagonalContainer[0] == 12:
        return 2

    return 0


# O(1)
def oppoDiagonalWinningVerification(oppoDiagonalContainer):
    if oppoDiagonalContainer[0] == 3:
        return 1
    if oppoDiagonalContainer[0] == 12:
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


def switchPlayer(player):
    if (player == 1):
        return int(2)
    elif (player == 2):
        return int(1)
    else:
        return int(0)
