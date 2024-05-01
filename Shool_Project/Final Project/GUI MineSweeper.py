
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
import configure
import random
from PIL import ImageTk, Image
from tkinter import messagebox


def start_screen_creation():

    def difficulty_picker(button_pressed):
        
        if button_pressed == 1:
            MineSweeper_window.destroy() #Closes the window. deiconify() shows it again
            main_game_screen(1)  # Difficulty Easy
        elif button_pressed == 2:
            MineSweeper_window.destroy()
            main_game_screen(2) #Difficulty Moderate
        elif button_pressed == 3:
            MineSweeper_window.destroy()
            main_game_screen(3) #Difficulty Hard

    # Creating a window for the game
    MineSweeper_window = tb.Window(themename = configure.THEME) 

    MineSweeper_window.geometry(f"{configure.WIDTH}x{configure.HEIGHT}")
    MineSweeper_window.title("Mine Sweeper")
    MineSweeper_window.resizable(False,False)

    #This makes lable (make sure to preinstall the font)
    game_lable = tk.Label(MineSweeper_window, 
                                text= "Mine Sweeper The Game",
                                font= configure.HEADER1_FONT) 
    
    #Creates the label and puts in on the screen
    game_lable.pack(padx=30,pady=30) 
   

    difficulty_button_easy = tk.Button(MineSweeper_window, 
                                       text="Easy --> 10 Mines",
                                       font= configure.HEADER2_FONT,
                                       command = lambda: difficulty_picker(1))
    
    difficulty_button_moderate = tk.Button(MineSweeper_window, 
                                           text="Moderate --> 20 Mines",
                                           font= configure.HEADER2_FONT,
                                           command = lambda: difficulty_picker(2))
    difficulty_button_hard = tk.Button(MineSweeper_window, 
                                       text="Hard --> 40 Mines", 
                                       font= configure.HEADER2_FONT,
                                       command = lambda: difficulty_picker(3))
    

    #Making a button, MAKE SURE THE FONT IS INSTALLED!
    difficulty_button_easy.pack(padx=10,pady=10) 
    difficulty_button_moderate.pack(padx=10,pady=10)
    difficulty_button_hard.pack(padx=10,pady=10)

    #Reads the scores from the file and sorts them from fastest to slowest
    with open('MineSweeper Times.txt','r') as times:
        all_times= times.readlines()
        
        easy_times = []
        moderate_times = []
        hard_times = []


        for line in all_times:
            if line.strip() and line.strip()[0]== 'e':
                time = line.strip()[1:]
                easy_times.append(int(time))
            if line.strip() and line.strip()[0]== 'm':
                time = line.strip()[1:]
                moderate_times.append(int(time))
            if line.strip() and line.strip()[0]== 'h':
                time = line.strip()[1:]
                hard_times.append(int(time))
                

    
    easy_times.sort()
    moderate_times.sort()
    hard_times.sort()
    values = 0

    #Formating the personal best times for the label

    personal_bests = 'Personal Bests\n\n\nEays Mode\n\n'
    for i in range(len(easy_times)):
        if values < 3: #Only want to display top three scores
            values += 1
            personal_bests+= f'{easy_times[i]} s\n'
       
    personal_bests += f'\n\nModerate Mode\n\n'
    for i in range(len(moderate_times)):
        values = 0
        if values < 3: #Only want to display top three scores
            values += 1
            personal_bests+= f'{moderate_times[i]} s\n'
    personal_bests += f'\n\nHard Mode\n\n'
    for i in range(len(hard_times)):
        values = 0
        if values < 3: #Only want to display top three scores
            values += 1
            personal_bests+= f'{hard_times[i]} s\n'
    

    best_times = tk.Label(master = MineSweeper_window, text = personal_bests, font=configure.HEADER2_FONT, justify='center')
    best_times.pack(padx=20,pady= 20, anchor='n')

    #Shows the window on the screen
    MineSweeper_window.mainloop() 

def main_game_screen(difficulty):
    
    global tiles_left, cheats_enabled, timer_on
    tiles_left = 64 #It is an 8x8 field
    cheats_enabled = False
    timer_on = True

    #Creates Unique mines coordinates
    def Unique_mines_coordinates():

        global number_of_mines
        global mines_locations
        global mine_counter #Created to not interfere with the number of mines

       
        mines_locations = set()

        if difficulty == 1:
            number_of_mines = 10
        elif difficulty == 2:
            number_of_mines = 20
        elif difficulty == 3:
            number_of_mines = 40

        mine_counter = number_of_mines

        while len(mines_locations) < number_of_mines :
            r = random.randint(0,7)
            c = random.randint(0,7)
            mines_locations.add((r,c))
            
    Unique_mines_coordinates()    

    main_game = tb.Window(themename = configure.THEME)
    main_game.geometry(f"{configure.WIDTH}x{configure.HEIGHT}")
    main_game.title("Mine Sweeper")
    

    #Mine fields
    grid_frame = tk.Frame()
    grid_frame.config(width=600,height=600,background= configure.FIELD_BG_COLOR)
    grid_frame.pack(padx= 5, pady= 5)

    #Warning sign image
    im = Image.open('assets/warning.png')
    resized = im.resize((60,60), Image.LANCZOS)
    warning_sign_image = ImageTk.PhotoImage(resized)

    def button_click(row, col):
        
        coordinates = (row,col)
        isMine = False
        number_of_mines_around_tile = 0
        global tiles_left, timer_on, time_elapsed
        
       
        if coordinates in mines_locations:
            isMine = True

        if isMine == True: #Mine found game over
            timer_on = False #Stops the timer
            cheats()    
            messagebox.showinfo('Game Over', 'You Clicked on a Mine')
            
                        
            main_game.destroy()
            start_screen_creation()
        
        else: #Not a mine
            if not buttons[row][col].cget('bg') == configure.FIELD_BG_COLOR: #Checks if the spot was already opened
                tiles_left -= 1
                if tiles_left == number_of_mines:
                    timer_on = False

                    #Writes the times on a txt file
                    with open('MineSweeper Times.txt', 'r') as times:
                        lines = times.readlines()

                    with open('MineSweeper Times.txt', 'w') as times:
                        for line in lines:
                            times.write(line)
                            if line.strip() == 'Easy:' and difficulty == 1:
                                times.write(f'e{time_elapsed}\n')
                            elif line.strip() == 'Moderate:' and difficulty == 2:
                                times.write(f'm{time_elapsed}\n')
                            elif line.strip() == 'Hard:' and difficulty == 3:
                                times.write(f'h{time_elapsed}\n')
                    
                    cheats() 
                    buttons[row][col].config(bg= configure.FIELD_BG_COLOR)
                    messagebox.showinfo('Congratulations', 'YOU WIN')
                    main_game.destroy()
                    start_screen_creation()

            #Checking top left
            if (row-1,col-1) in mines_locations:
                number_of_mines_around_tile += 1

            #Checking top center
            if (row-1,col) in mines_locations:
                number_of_mines_around_tile += 1

            #Checking top right
            if (row-1,col+1) in mines_locations:
                number_of_mines_around_tile += 1
            
            #Checking left
            if (row,col-1) in mines_locations:
                number_of_mines_around_tile += 1
            
            #Checking right
            if (row,col+1) in mines_locations:
                number_of_mines_around_tile += 1
            
            #Checking bottom left
            if (row+1,col-1) in mines_locations:
                number_of_mines_around_tile += 1
            
            #Checking bottom center
            if (row+1,col) in mines_locations:
                number_of_mines_around_tile += 1
            
            #Checking bottom right
            if (row+1,col+1) in mines_locations:
                number_of_mines_around_tile += 1

            #Clears the spot if it was not already cleared         
            buttons[row][col].config(bg= configure.FIELD_BG_COLOR, text= number_of_mines_around_tile, font = configure.MINE_FONT) 

            #Sets the appropriate number color
            if number_of_mines_around_tile == 1:
                buttons[row][col].config(fg = 'blue')
            elif number_of_mines_around_tile == 2:
                buttons[row][col].config(fg = 'green')
            elif number_of_mines_around_tile == 3:
                buttons[row][col].config(fg = 'red')
            elif number_of_mines_around_tile == 4:
                buttons[row][col].config(fg = 'purple')
            elif number_of_mines_around_tile == 5 or number_of_mines_around_tile == 6 or number_of_mines_around_tile == 7 or number_of_mines_around_tile == 8:
                buttons[row][col].config(fg = 'Yellow')
                 

    def on_right_click(event):
        global mine_counter

        current_image = event.widget.cget('image')
        if current_image == '':
            event.widget.config(image = warning_sign_image)
            mine_counter -= 1
            mines_left.config(text= f'Mines Remaining: {mine_counter}')
        else:
            event.widget.config(image= '')
            mine_counter += 1
            mines_left.config(text= f'Mines Remaining: {mine_counter}')
       

    #Mine image
    button_image = Image.open('assets/mine.png')
    resized = button_image.resize((60,60), Image.LANCZOS)
    new_mine = ImageTk.PhotoImage(resized)
    
    #Hover effect
    def on_enter(event):
        bg_color = event.widget.cget('bg')
        
        if not bg_color == configure.FIELD_BG_COLOR: #Checks if the bg colo matches the field and if it does it doesn't do the hover effect
            event.widget.config(bg= '#50C878')

    def on_leave(event):
        bg_color = event.widget.cget('bg')
        
        if not bg_color == configure.FIELD_BG_COLOR:
            event.widget.config(bg = configure.FIELD_FG_COLOR)

    # Create buttons in a loop and place them in a grid
    buttons = []
    for row in range(8):
        button_row = []
        for col in range(8):
            button = tk.Button(grid_frame, text="", height=3, width=5, command=lambda row=row, col=col: button_click(row, col))
            button.config(bg= configure.FIELD_FG_COLOR, font= configure.MINE_FONT)
            button.grid(row=row, column=col, padx=3, pady=3, sticky = 'news')
            
            button.bind('<Button-3>', on_right_click)
            button.bind("<Enter>", on_enter)
            button.bind("<Leave>", on_leave)

            button_row.append(button)
        buttons.append(button_row)

    mines_left = tk.Label(master = main_game, text= f'Mines Remaining: {number_of_mines}',font= configure.HEADER2_FONT)
    mines_left.pack(padx= 10,pady= 10,side= 'top', anchor= 'nw',)

    def cheats():
        
        global cheats_enabled
        #Checks to see if the cheats are enabled and then reveals the mines
        
        if cheats_enabled == False:
            for r,c in mines_locations:
                #Asigns mines to the buttons
                buttons[r][c].config(image = new_mine)
            cheats_enabled = True

        else:
            for r in range(8):
                for c in range (8):
                    buttons[r][c].config(image = '')
            
            cheats_enabled = False


        


    cheat_button = tk.Button(master = main_game, text = 'Reveal mines', font = configure.REVEAL_MINES_FONT, command = cheats)
    

    
    global time_elapsed
    time_elapsed = 0
    

    timer_label = tk.Label(master = main_game, text = 'Time: 0', font= configure.HEADER2_FONT)
    timer_label.pack(padx= 10, pady= 10, anchor='w')
    cheat_button.pack(padx = 10, pady = 10, anchor='nw')

    def update_timer():
        global time_elapsed,timer_on

        if timer_on:
            time_elapsed += 1
            timer_label.config(text= f'Time: {time_elapsed}')
            main_game.after(1000, update_timer) #Function is called every second

    

    update_timer() #Run the timer

    main_game.mainloop()


if __name__ == "__main__":
    
    start_screen_creation()
    