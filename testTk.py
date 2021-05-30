# -*- coding: utf-8 -*-
import tkinter as tk
from backend import *


class Game(tk.Frame):
    def __init__(self, master):
        super(Game, self).__init__(master)
        self.width = 300
        self.height = 340
        self.canvas = tk.Canvas(self, bg='#98ffcc',
                                width=self.width,
                                height=self.height)
        self.canvas.create_line(0, 40, 300, 40)
        self.canvas.create_line(0, 140, 300, 140)
        self.canvas.create_line(100, 40, 100, 340)
        self.canvas.create_line(0, 240, 300, 240)
        self.canvas.create_line(200, 40, 200, 340)
        self.canvas.bind('<Button-1>', motion)
        self.canvas.pack()
        self.pack()

def motion(event):
  print("Mouse position: (%s %s)" % (event.x, event.y))
  return

if __name__ == '__main__':
    root = tk.Tk()
    root.resizable(False, False)
    root.title('Tic Tac Toe Game')
    game = Game(root)
    game.mainloop()





