import tkinter as tk
import ttkbootstrap as tb
from subprocess import call #makes it possible to run .py files inside this file
import configure

def main():

    console_screen = tb.Window(themename= 'morph')
    console_screen.title('Gaming Console')
    console_screen.geometry('700x300')

    

    title_label = tk.Label(master= console_screen, text= 'Gaming Console', font= configure.HEADER1_FONT)
    title_label.pack(padx= 10, pady= 10)

    grid_frame = tk.Frame()
    grid_frame.config(width=600,height=600)
    grid_frame.pack(padx= 20, pady= 20)

    def minesweeper_game():
        call(['python', 'GUI MineSweeper.py'])

    def rps_game():
        call(['python', 'rps.py'])

    def dominos_game():
        call(['python', 'Domino_GUI.py'])

    def bj_game():
        call(['python', 'Black_Jack_GUI.py'])

    minesweeper_button = tk.Button(master= grid_frame, text= 'Mine Sweeper', font= configure.HEADER2_FONT, command= minesweeper_game)

    rps_button = tk.Button(master= grid_frame, text= 'Rock Paper Scissors', font= configure.HEADER2_FONT, command= rps_game)

    dominos_button = tk.Button(master= grid_frame, text= 'Dominos', font= configure.HEADER2_FONT, command= dominos_game)

    bj_button = tk.Button(master= grid_frame, text= 'Black Jack', font= configure.HEADER2_FONT, command= bj_game)
 

    minesweeper_button.grid(row= 0, column=0, sticky='news', padx=5, pady= 5)
    rps_button.grid(row= 0, column=1, sticky='news', padx=5, pady= 5)
    dominos_button.grid(row= 1, column=0, sticky='news', padx=5, pady= 5)
    bj_button.grid(row= 1, column=1, sticky='news', padx=5, pady= 5)


    creator_label = tk.Label(master= console_screen, text='Created by: Klei Nagode and Alfredo Capacho', font= ('Calibri', 12), justify= 'left')
    creator_label.pack(padx=5, pady= 5, anchor='nw')
    

    console_screen.mainloop()


if __name__ == '__main__':
    main()

