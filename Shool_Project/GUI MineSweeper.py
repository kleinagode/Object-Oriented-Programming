
import tkinter as tk
import ttkbootstrap as ttk


def start_screen_creation():

    def difficulty_picker(button_pressed):
        #Not finished
        #When done this function will open up another widow with the game and it's difficulty set
        if button_pressed == 1:
            print(1)  # Difficulty Easy
        elif button_pressed == 2:
            print(2) #Difficulty Moderate
        elif button_pressed == 3:
            print(3) #Difficulty Hard
    
    # Creating a window for the game
    MineSweeper_window = ttk.Window(themename = 'morph') 

    MineSweeper_window.geometry("1000x800")
    MineSweeper_window.title("Mine Sweeper")

    #This makes lable (make sure to preinstall the font)
    game_lable = tk.Label(MineSweeper_window, 
                                text= "Mine Sweeper The Game",
                                font= ("Zig",30)) 
    
    #Creates the label and puts in on the screen
    game_lable.pack(padx=30,pady=30) 
   

    difficulty_button_easy = tk.Button(MineSweeper_window, 
                                       text="Easy --> 10 Mines",
                                       font= ("White Rabbit",18),
                                       command = lambda: difficulty_picker(1))
    
    difficulty_button_moderate = tk.Button(MineSweeper_window, 
                                           text="Moderate --> 20 Mines",
                                           font= ("White Rabbit",18),
                                           command = lambda: difficulty_picker(2))
    difficulty_button_hard = tk.Button(MineSweeper_window, 
                                       text="Hard --> 40 Mines", 
                                       font= ("White Rabbit",18),
                                       command = lambda: difficulty_picker(3))
    
    #Making a button, MAKE SURE THE FONT IS INSTALLED!
    difficulty_button_easy.pack(padx=10,pady=10) 
    difficulty_button_moderate.pack(padx=10,pady=10)
    difficulty_button_hard.pack(padx=10,pady=10)

    #Shows the window on the screen
    MineSweeper_window.mainloop() 


if __name__ == "__main__":
    
    start_screen_creation()