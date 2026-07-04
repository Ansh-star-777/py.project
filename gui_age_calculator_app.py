import tkinter as tk
from datetime import date

window = tk.Tk()
window.title("Age Calculator App")
window.geometry("400x400")

tk.Label(window, text="Name:").grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(window, text="Date:").grid(row=1, column=0, padx=10, pady=10)
date_entry = tk.Entry(window)
date_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(window, text="Month:").grid(row=2, column=0, padx=10, pady=10)
month_entry = tk.Entry(window)
month_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(window, text="Year:").grid(row=3, column=0, padx=10, pady=10)
year_entry = tk.Entry(window)
year_entry.grid(row=3, column=1, padx=10, pady=10)

def calculate_age():
    name = name_entry.get()
    day = int(date_entry.get())
    month = int(month_entry.get())
    year = int(year_entry.get())

    today = date.today()
    age = today.year - year

    if (today.month, today.day) < (month, day):
        age -= 1

    message = f"Hello {name}, you are {age} years old!"
    result_label.config(text=message)

calc_button = tk.Button(window, text="Calculate Age", command=calculate_age)
calc_button.grid(row=4, column=0, columnspan=2, pady=15)

result_label = tk.Label(window, text="", wraplength=300)
result_label.grid(row=5, column=0, columnspan=2, pady=10)

window.mainloop()
