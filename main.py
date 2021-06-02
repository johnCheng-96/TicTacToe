# -*- coding: utf-8 -*-
import time
from tkinter import *
import tkinter as tk
from backend import *


class Game(tk.Frame):
    def __init__(self, master):
        super(Game, self).__init__(master)
        self.width = 300
        self.height = 300
        self.moveCounter = 0
        self.labelBin = []
        self.status = 0
        self.lineCanvas = tk.Canvas(self, bg='#98ffcc',
                                    width=self.width,
                                    height=self.height, bd=0, highlightthickness=0)

        # self.canvas = tk.Canvas(self, bg='#98ffcc',
        #                         width=self.width,
        #                         height=self.height, bd=0, highlightthickness=0)
        # self.canvas.create_line(0, 0, 300, 0)
        self.drawGrid()
        self.lineCanvas.bind('<Button-1>', self.motion)
        self.lineCanvas.pack()
        self.pack()

        self.board, self.rowsContainer, self.colsContainer, self.diagonalContainer, self.oppoDiagonalContainer, self.player = init()

    def drawGrid(self):
        self.lineCanvas.create_line(0, 100, 300, 100)
        self.lineCanvas.create_line(100, 0, 100, 300)
        self.lineCanvas.create_line(0, 200, 300, 200)
        self.lineCanvas.create_line(200, 0, 200, 300)

    def endGameProcess(self, text):
        msg = tk.Label(self, text=text, font=("Arial", 49))
        if (self.status > 0):
            msg.place(x=0, y=100)
        else:
            msg.place(x=110, y=120)

        self.labelBin.append(msg)
        self.createAnotherGameButton()


    def convertMouseLocToRowNCol(self, x, y):
        if (x < 100):
            colNum = 0
        elif (x >= 100 and x < 200):
            colNum = 1
        elif (x >= 200 and x < 300):
            colNum = 2

        if (y < 100):
            rowNum = 0
        elif (y >= 100 and y < 200):
            rowNum = 1
        elif (y >= 200 and y < 300):
            rowNum = 2

        return rowNum, colNum

    def motion(self, event):

        x = event.x
        y = event.y

        rowNum, colNum = self.convertMouseLocToRowNCol(x, y)

        ''' if the place is occupied '''
        if (self.board[rowNum][colNum] != 0):
            return

        makeMoke(self.board, self.player, colNum, rowNum, self.rowsContainer, self.colsContainer,
                 self.diagonalContainer, self.oppoDiagonalContainer)

        if (self.player == 1):
            piece = "×"
            yAdjust = 8
        elif (self.player == 2):
            piece = "○"
            yAdjust = 3

        theMove = tk.Label(self, text=piece, bg='#98ffcc', font=("Arial", 70), bd=0, highlightthickness=0)
        self.labelBin.append(theMove)
        theMove.place(x=colNum * 100 + 28, y=rowNum * 100 + yAdjust)
        self.moveCounter += 1
        self.status = winningVerification(self.rowsContainer, self.colsContainer, self.diagonalContainer,
                                          self.oppoDiagonalContainer)

        if (self.status):
            if (self.status == 1):
                gameWinner = "1"

            if (self.status == 2):
                gameWinner = "2"

            text = "Player " + gameWinner + " won!"
            self.endGameProcess(text)

        else:
            if (self.moveCounter == 9):
                text = "Tie!"

                self.endGameProcess(text)


        self.player = switchPlayer(self.player)

    def resetGame(self):
        for label in self.labelBin:
            label.destroy()
        self.resetButton.destroy()
        self.board, self.rowsContainer, self.colsContainer, self.diagonalContainer, self.oppoDiagonalContainer, self.player = init()
        self.moveCounter = 0
        self.labelBin = []
        self.status = 0





    def createAnotherGameButton(self):
        buttonText = "Another Game"
        self.resetButton = tk.Button(self, text=buttonText, fg='red', highlightbackground='DarkBlue', command=self.resetGame)
        self.resetButton.place(x=90, y=200)

            # nextGameFlag = input("Still want to play? (y/n) : ")
            # if (nextGameFlag.lower() != "y"):
            # reset after win, or tie
            # break
            # self.board, self.rowsContainer, self.colsContainer, self.diagonalContainer, self.oppoDiagonalContainer, self.player = init()

            # no one win switch player




    def displayBoardAs2D(self):
        print(self.board[0])
        print(self.board[1])
        print(self.board[2])
        print()


# board, rowsContainer, colsContainer, diagonalContainer, oppoDiagonalContainer, player
def init():
    return createboard(), createRowsContainer(), createColsContainer(), createDiagonalContainer(), createOppoDiagonalContainer(), 1


if __name__ == '__main__':

    # board, rowsContainer, colsContainer, diagonalContainer, oppoDiagonalContainer, player = init()

    root = tk.Tk()
    root.resizable(False, False)
    root.title('Tic Tac Toe Game')
    game = Game(root)
    game.mainloop()

    # init
    # board, rowsContainer, colsContainer, diagonalContainer, oppoDiagonalContainer, player = init()

    # # gameflow
    # print("Welcome to Tic Tac Toe game")
    # while (True):
    #
    #     print("Player : " + str(player))
    #     # displayBoardAs2D()
    #
    #     # user input, x is colNum, y is rowNum
    #     move = input("Please place your move (in format rowNum,colNum) \n")
    #     rowNum, colNum = move.split(',')
    #
    #     colNum = int(colNum)
    #     rowNum = int(rowNum)
    #
    #     # place userInput into move method
    #
    #     makeMoke(board, player, colNum, rowNum, rowsContainer, colsContainer, diagonalContainer, oppoDiagonalContainer)
    #
    #     # displayBoardAs2D()
    #
    #     # next game query
    #
    #     status = winningVerification(rowsContainer, colsContainer, diagonalContainer, oppoDiagonalContainer)
    #     if (status):
    #         if (status == 1):
    #             print("player X won!")
    #             winner = "1"
    #
    #         if (status == 2):
    #             print("player O won!")
    #             winner = "2"
    #         msg = tk.Label("Player " + winner + " won!")
    #         msg.place()
    #         nextGameFlag = input("Still want to play? (y/n) : ")
    #         if (nextGameFlag.lower() != "y"):
    #             # reset after win, or tie
    #             break
    #         board, rowsContainer, colsContainer, diagonalContainer, oppoDiagonalContainer, player = init()
    #     else:
    #
    #         # no one win switch player
    #         player = switchPlayer(player)
