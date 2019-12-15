#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox

# 0 = empty
# 1 = X
# 2 = 0

comp = True
turn = 1
winner = 0

empty = ((0, 0, 0),
         (0, 0, 0),
         (0, 0, 0))

a = empty  # copy


def calc_states(state, t):
    states = []

    for x in range(9):
        if not state[x // 3][x % 3]:
            li = [list(y) for y in state]
            li[x // 3][x % 3] = t
            states.append(tuple(tuple(y) for y in li))

    return states


def maximize(s):
    states = calc_states(s, 2)
    states_values = []
    for n, state in enumerate(states):
        if check(state):
            states_values.append(({1: -1, 2: 1, 0: 0, 3: 0}[check(state)], state))
        else:
            states_values.append((minimize(state)[0], state))
    x = [y[0] for y in states_values]
    return states_values[x.index(max(x))]


def minimize(s):
    states = calc_states(s, 1)
    states_values = []
    for n, state in enumerate(states):
        if check(state):
            states_values.append(({1: -1, 2: 1, 0: 0, 3: 0}[check(state)], state))
        else:
            states_values.append((maximize(state)[0], state))
    x = [y[0] for y in states_values]
    return states_values[x.index(min(x))]


def minimax(s):
    return maximize(s)


def declare(n):
    """Declare Winner"""
    global winner
    winner = n


def check(s):
    """Check for any winners"""
    # horizontal checks
    for r in s:
        if r[0] == r[1] == r[2] != 0:
            return r[0]

    # vertical checks
    for x in range(3):
        if s[0][x] == s[1][x] == s[2][x] != 0:
            return s[0][x]

    # diagonal checks
    if s[0][0] == s[1][1] == s[2][2] != 0:
        return s[1][1]
    if s[0][2] == s[1][1] == s[2][0] != 0:
        return s[1][1]

    # draw
    if 0 not in s[0] + s[1] + s[2]:
        return 3

    return 0


def xo(n):
    x = {0: '', 1: '×', 2: '○'}[n]
    return x


def pretty_print(s):
    print(" %s │ %s │ %s" % (xo(s[0][0]), xo(s[0][1]), xo(s[0][2])))
    print("───┼───┼───")
    print(" %s │ %s │ %s" % (xo(s[1][0]), xo(s[1][1]), xo(s[1][2])))
    print("───┼───┼───")
    print(" %s │ %s │ %s\n" % (xo(s[2][0]), xo(s[2][1]), xo(s[2][2])))


def get_mark(pos):
    return a[pos // 3][pos % 3]


def mark(pos):
    global a, turn
    x = [list(y) for y in a]  # tuple to list
    x[pos // 3][pos % 3] = turn
    a = tuple(tuple(y) for y in x)  # list to tuple
    turn = 2 if turn is 1 else 1


def make_mark():
    global a, turn
    a = minimax(a)[1]
    turn = 2 if turn is 1 else 1


def gui():
    def reset():
        global a, turn, winner
        a = empty
        for x in buttons:
            x.config(text='', state=tk.NORMAL)
        turn = 1
        winner = 0
        current_turn.config(text=xo(turn) + "'s turn")

    def win():
        messagebox.showinfo("Game Ended.", "Game drawed." if winner == 3 else xo(winner) + " won the game")
        reset()

    def press(n):
        mark(n)
        if comp:
            declare(check(a))  # check for player win if computer is playing
            if not winner:
                make_mark()
        for n, button in enumerate(buttons):
            value = get_mark(n)
            button.config(text=xo(value), state=tk.DISABLED if value else tk.NORMAL)
        declare(check(a))
        if winner:
            win()
        current_turn.config(text=xo(turn) + "'s turn")

    def switch_mode():
        global comp
        comp = not comp
        if comp:
            menu.entryconfigure(2, label="Human vs. Computer")
        else:
            menu.entryconfigure(2, label="Human vs. Human")
        reset()

    root = tk.Tk()

    menu = tk.Menu(root)
    menu.add_command(label="New Game", command=reset)
    menu.add_command(label="Human vs. Computer", command=switch_mode)

    root.config(menu=menu)
    root.title("TicTacToe")
    root.geometry("300x320")
    root.resizable(False, False)

    # buttons
    zero = tk.Button(root, font=('', 32), fg='white', disabledforeground='white', bg='gray50',
                     activebackground='gray60', command=lambda: press(0))
    one = tk.Button(root, font=('', 32), fg='white', disabledforeground='white', bg='gray50',
                    activebackground='gray60', command=lambda: press(1))
    two = tk.Button(root, font=('', 32), fg='white', disabledforeground='white', bg='gray50',
                    activebackground='gray60', command=lambda: press(2))
    three = tk.Button(root, font=('', 32), fg='white', disabledforeground='white', bg='gray50',
                      activebackground='gray60', command=lambda: press(3))
    four = tk.Button(root, font=('', 32), fg='white', disabledforeground='white', bg='gray50',
                     activebackground='gray60', command=lambda: press(4))
    five = tk.Button(root, font=('', 32), fg='white', disabledforeground='white', bg='gray50',
                     activebackground='gray60', command=lambda: press(5))
    six = tk.Button(root, font=('', 32), fg='white', disabledforeground='white', bg='gray50',
                    activebackground='gray60', command=lambda: press(6))
    seven = tk.Button(root, font=('', 32), fg='white', disabledforeground='white', bg='gray50',
                      activebackground='gray60', command=lambda: press(7))
    eight = tk.Button(root, font=('', 32), fg='white', disabledforeground='white', bg='gray50',
                      activebackground='gray60', command=lambda: press(8))

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
