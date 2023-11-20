import tkinter as tk
from tkinter import Radiobutton, IntVar

def calculate():
    side = float(s.get())
    d1 = float(d1_entry.get())
    d2 = float(d2_entry.get())

    if operation.get() == 1: 
        area = 0.5 * d1 * d2
        result_label.config(text=f"Площа ромба: {area:.2f} кв. од.")
    elif operation.get() == 2:  
        p = 4 * side
        result_label.config(text=f"Периметр ромба: {p:.2f} од.")
    else:
        result_label.config(text="Оберіть операцію")

app = tk.Tk()
app.title("Обчислення периметру та площі ромба")

tk.Label(app, text="Введіть сторону ромба:").grid(row=0, column=0, pady=10)
s = tk.Entry(app)
s.grid(row=0, column=1, pady=10)

tk.Label(app, text="Введіть першу діагональ:").grid(row=1, column=0, pady=10)
d1_entry = tk.Entry(app)
d1_entry.grid(row=1, column=1, pady=10)

tk.Label(app, text="Введіть другу діагональ:").grid(row=2, column=0, pady=10)
d2_entry = tk.Entry(app)
d2_entry.grid(row=2, column=1, pady=10)

operation = IntVar()
operation.set(0)

tk.Radiobutton(app, text="Площа", variable=operation, value=1).grid(row=3, column=0, pady=10)
tk.Radiobutton(app, text="Периметр", variable=operation, value=2).grid(row=3, column=1, pady=10)

calculate_button = tk.Button(app, text="Обчислити", command=calculate)
calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

result_label = tk.Label(app, text="")
result_label.grid(row=5, column=0, columnspan=2, pady=10)

app.mainloop()
