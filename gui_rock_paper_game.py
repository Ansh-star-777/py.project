import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]

def play(user_choice):
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    computer_label.config(text="Computer chose: " + computer_choice)
    result_label.config(text=result)

window = tk.Tk()
window.title("Rock Paper Scissors Game")
window.geometry("400x400")

heading_label = tk.Label(window, text="Rock Paper Scissors", font=("Arial", 16, "bold"))
heading_label.pack(pady=20)

instruction_label = tk.Label(window, text="Click a button to make your choice:", font=("Arial", 12))
instruction_label.pack(pady=10)

button_frame = tk.Frame(window)
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_button.grid(row=0, column=2, padx=5)

computer_label = tk.Label(window, text="Computer chose: ", font=("Arial", 12))
computer_label.pack(pady=20)

result_label = tk.Label(window, text="", font=("Arial", 14, "bold"), fg="blue")
result_label.pack(pady=10)

window.mainloop()
