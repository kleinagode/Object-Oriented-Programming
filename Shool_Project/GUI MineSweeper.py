
import tkinter as tk


def window_creation():
    MineSweeper_window = tk.Tk() # Creating a window for the game

    MineSweeper_window.geometry("1000x800")
    MineSweeper_window.title("Mine Sweeper")

    game_lable = tk.Label(MineSweeper_window, 
                                text= "Mine Sweeper The Game",
                                font= ("Zig",30)) #This makes lable (make sure to preinstall the font)
    
    game_lable.pack(padx=30,pady=30) #Creates the label and puts in on the screen
   
    difficulty_button_easy = tk.Button(MineSweeper_window, text="Easy --> 10 Mines",
                                   font= ("White Rabbit",18))
    difficulty_button_moderate = tk.Button(MineSweeper_window, text="Moderate --> 20 Mines",
                                   font= ("White Rabbit",18))
    difficulty_button_hard = tk.Button(MineSweeper_window, text="Hard --> 40 Mines",
                                   font= ("White Rabbit",18))
    

    difficulty_button_easy.pack(padx=10,pady=10) #Making a button, MAKE SURE THE FONT IS INSTALLED!
    difficulty_button_moderate.pack(padx=10,pady=10)
    difficulty_button_hard.pack(padx=10,pady=10)


    MineSweeper_window.mainloop() #Shows the window on the screen


if __name__ == "__main__":
    
    window_creation()