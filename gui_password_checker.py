import tkinter as tk

window = tk.Tk()
window.title("Length Converter App")
window.geometry("400x400")

tk.Label(window, text="Enter Password:").pack(pady=10)
password_entry = tk.Entry(window, show="*")
password_entry.pack(pady=5)

def check_strength():
    password = password_entry.get()
    length = len(password)

    if length <= 5:
        strength = "Weak"
        color = "red"
    elif length <= 8:
        strength = "Medium"
        color = "yellow"
    elif length <= 12:
        strength = "Strong"
        color = "light green"
    else:
        strength = "Very Strong"
        color = "dark green"

    result_label.config(text=f"Strength: {strength}", fg=color)

check_button = tk.Button(window, text="Check Strength", command=check_strength)
check_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack(pady=20)

window.mainloop()
