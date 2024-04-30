import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")

        self.player_score = 0
        self.computer_score = 0

        self.player_choice = ""
        self.computer_choice = ""

        self.player_label = tk.Label(root, text="Player: 0", font=("Helvetica", 16))
        self.player_label.grid(row=0, column=0, padx=10, pady=10)

        self.computer_label = tk.Label(root, text="Computer: 0", font=("Helvetica", 16))
        self.computer_label.grid(row=0, column=1, padx=10, pady=10)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.result_label.grid(row=1, columnspan=2, padx=10, pady=10)

        self.rock_image = tk.PhotoImage(file="rock.png").subsample(3, 3)
        self.rock_button = tk.Button(root, image=self.rock_image, command=lambda: self.play("rock"))
        self.rock_button.grid(row=2, column=0, padx=10, pady=10)

        self.paper_image = tk.PhotoImage(file="paper.png").subsample(3, 3)
        self.paper_button = tk.Button(root, image=self.paper_image, command=lambda: self.play("paper"))
        self.paper_button.grid(row=2, column=1, padx=10, pady=10)

        self.scissors_image = tk.PhotoImage(file="scissors.png").subsample(5, 5)
        self.scissors_button = tk.Button(root, image=self.scissors_image, command=lambda: self.play("scissors"))
        self.scissors_button.grid(row=3, columnspan=2, padx=10, pady=10)

    def play(self, player_choice):
        self.player_choice = player_choice
        self.computer_choice = random.choice(["rock", "paper", "scissors"])

        if self.player_choice == self.computer_choice:
            self.result_label.config(text="It's a tie!")
        elif (self.player_choice == "rock" and self.computer_choice == "scissors") or \
             (self.player_choice == "paper" and self.computer_choice == "rock") or \
             (self.player_choice == "scissors" and self.computer_choice == "paper"):
            self.result_label.config(text="You win!")
            self.player_score += 1
        else:
            self.result_label.config(text="Computer wins!")
            self.computer_score += 1

        self.update_score()

    def update_score(self):
        self.player_label.config(text=f"Player: {self.player_score}")
        self.computer_label.config(text=f"Computer: {self.computer_score}")

root = tk.Tk()
game = RockPaperScissorsGame(root)
root.mainloop()
