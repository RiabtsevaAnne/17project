import tkinter as tk
import math

def calculate():
    length = float(entry.get())

    area = (3 * math.sqrt(3) / 2) * length**2

    result.config(text=f"Площа шестикутника: {area:.2f} кв. од.")

app = tk.Tk()
app.title("Обчислення площі шестикутника")

label = tk.Label(app, text="Введіть довжину сторони шестикутника:")
label.pack(pady=10)

entry = tk.Entry(app)
entry.pack(pady=10)

button = tk.Button(app, text="Обчислити площу", command=calculate)
button.pack(pady=10)

result = tk.Label(app, text="")
result.pack(pady=10)

app.mainloop()
