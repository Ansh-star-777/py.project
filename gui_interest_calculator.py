import tkinter as tk

window = tk.Tk()
window.title("Interest Calculator App")
window.geometry("400x400")

tk.Label(window, text="Principle:").grid(row=0, column=0, padx=10, pady=10)
principle_entry = tk.Entry(window)
principle_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(window, text="Time (years):").grid(row=1, column=0, padx=10, pady=10)
time_entry = tk.Entry(window)
time_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(window, text="Rate (%):").grid(row=2, column=0, padx=10, pady=10)
rate_entry = tk.Entry(window)
rate_entry.grid(row=2, column=1, padx=10, pady=10)

def calculate_interest():
    p = float(principle_entry.get())
    t = float(time_entry.get())
    r = float(rate_entry.get())

    simple_interest = (p * t * r) / 100
    compound_interest = p * ((1 + r / 100) ** t) - p

    result_label.config(
        text=f"Simple Interest: {simple_interest:.2f}\nCompound Interest: {compound_interest:.2f}"
    )

calc_button = tk.Button(window, text="Calculate Interest", command=calculate_interest)
calc_button.grid(row=3, column=0, columnspan=2, pady=15)

result_label = tk.Label(window, text="", wraplength=300)
result_label.grid(row=4, column=0, columnspan=2, pady=10)

window.mainloop()
