#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox

# 0 = empty
# 1 = X
# 2 = 0

turn = 1
winner = 0

array = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

a = array.copy()


def declare(n):
    """Declare Winner"""
    global winner
    winner = n


def check():
    """Check for any winners"""
    # horizontal checks
    for r in a:
        if r[0] == r[1] == r[2] != 0:
            declare(r[0])

    # vertical checks
    for x in range(3):
        if a[0][x] == a[1][x] == a[2][x] != 0:
            declare(a[0][x])

    # diagonal checks
    if a[0][0] == a[1][1] == a[2][2] != 0:
        declare(a[1][1])
    if a[0][2] == a[1][1] == a[2][0] != 0:
        declare(a[1][1])

    # draw
    if 0 not in a[0] + a[1] + a[2]:
        declare(3)


def xo(n):
    x = {0: ' ', 1: '×', 2: '○'}[n]
    return x


def pretty_print():
    print(" %s │ %s │ %s" % (xo(a[0][0]), xo(a[0][1]), xo(a[0][2])))
    print("───┼───┼───")
    print(" %s │ %s │ %s" % (xo(a[1][0]), xo(a[1][1]), xo(a[1][2])))
    print("───┼───┼───")
    print(" %s │ %s │ %s" % (xo(a[2][0]), xo(a[2][1]), xo(a[2][2])))


def mark(pos):
    global turn
    a[pos // 3][pos % 3] = turn
    turn = 2 if turn is 1 else 1


def gui():

    def reset():
        global a, turn, winner
        a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for x in buttons:
            x.config(text='', state=tk.NORMAL)
        turn = 1
        winner = 0
        current_turn.config(text=xo(turn) + "'s turn")

    def win():
        messagebox.showinfo("Game Ended.", "Game drawed." if winner == 3 else xo(winner) + " won the game")
        reset()

    def press(n):
        buttons[n].config(text=xo(turn), state=tk.DISABLED)
        mark(n)
        check()
        if winner:
            win()
        current_turn.config(text=xo(turn) + "'s turn")

    root = tk.Tk()

    menu = tk.Menu(root)
    menu.add_command(label="New Game", command=reset)

    root.config(menu=menu)
    root.title("TicTacToe")
    root.geometry("300x320")
    root.resizable(False, False)

    # buttons
    zero = tk.Button(root, font=('', 32), disabledforeground='black', command=lambda: press(0))
    one = tk.Button(root, font=('', 32), disabledforeground='black', command=lambda: press(1))
    two = tk.Button(root, font=('', 32), disabledforeground='black', command=lambda: press(2))
    three = tk.Button(root, font=('', 32), disabledforeground='black', command=lambda: press(3))
    four = tk.Button(root, font=('', 32), disabledforeground='black', command=lambda: press(4))
    five = tk.Button(root, font=('', 32), disabledforeground='black', command=lambda: press(5))
    six = tk.Button(root, font=('', 32), disabledforeground='black', command=lambda: press(6))
    seven = tk.Button(root, font=('', 32), disabledforeground='black', command=lambda: press(7))
    eight = tk.Button(root, font=('', 32), disabledforeground='black', command=lambda: press(8))

    zero.place(x=0, y=0, height=100, width=100)
    one.place(x=100, y=0, height=100, width=100)
    two.place(x=200, y=0, height=100, width=100)
    three.place(x=0, y=100, height=100, width=100)
    four.place(x=100, y=100, height=100, width=100)
    five.place(x=200, y=100, height=100, width=100)
    six.place(x=0, y=200, height=100, width=100)
    seven.place(x=100, y=200, height=100, width=100)
    eight.place(x=200, y=200, height=100, width=100)

    buttons = [zero, one, two, three, four, five, six, seven, eight]

    current_turn = tk.Label(root, text="×'s turn")
    current_turn.place(x=0, y=300)

    root.mainloop()


if __name__ == '__main__':
    gui()
