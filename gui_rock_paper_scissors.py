import tkinter as tk
import random

window = tk.Tk()
window.title("Length Converter App")
window.geometry("400x400")

choices = ["Rock", "Paper", "Scissors"]

def play(user_choice):
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    result_label.config(
        text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}"
    )

tk.Label(window, text="Choose your move:", font=("Arial", 14)).pack(pady=20)

rock_button = tk.Button(window, text="Rock", width=15, command=lambda: play("Rock"))
rock_button.pack(pady=5)

paper_button = tk.Button(window, text="Paper", width=15, command=lambda: play("Paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(window, text="Scissors", width=15, command=lambda: play("Scissors"))
scissors_button.pack(pady=5)

result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=20)

window.mainloop()
