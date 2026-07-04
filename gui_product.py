import tkinter as tk

window = tk.Tk()
window.title("Getting Started with Widgets")
window.geometry("400x300")

info_label = tk.Label(window, text="This app multiplies two numbers you enter.")
info_label.pack(pady=5)

label1 = tk.Label(window, text="Enter first number:")
label1.pack()

entry1 = tk.Entry(window)
entry1.pack()

label2 = tk.Label(window, text="Enter second number:")
label2.pack()

entry2 = tk.Entry(window)
entry2.pack()

def calculate_product():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 * num2

    result_box.delete(1.0, tk.END)
    result_box.insert(tk.END, result)

calc_button = tk.Button(window, text="Calculate Product", command=calculate_product)
calc_button.pack(pady=5)

result_box = tk.Text(window, height=1, width=20)
result_box.pack(pady=5)

window.mainloop()
