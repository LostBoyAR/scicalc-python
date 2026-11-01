"""SciCalc - Scientific Calculator using Python Tkinter (angles in degrees)."""
import math
import tkinter as tk

# Allowed functions and constants (safe evaluation)
SAFE = {
    "sin": lambda x: math.sin(math.radians(x)),
    "cos": lambda x: math.cos(math.radians(x)),
    "tan": lambda x: math.tan(math.radians(x)),
    "log": math.log10, "ln": math.log, "sqrt": math.sqrt,
    "fact": math.factorial, "pi": math.pi, "e": math.e,
}

root = tk.Tk()
root.title("SciCalc - Scientific Calculator")
root.resizable(False, False)
screen = tk.Entry(root, font=("Arial", 22), justify="right", bd=8, bg="#f0f4f8")
screen.grid(row=0, column=0, columnspan=5, padx=6, pady=6, sticky="nsew")


def press(key):
    if key == "C":
        screen.delete(0, tk.END)
    elif key == "DEL":
        screen.delete(len(screen.get()) - 1, tk.END)
    elif key == "=":
        try:
            result = eval(screen.get().replace("^", "**"), {"__builtins__": {}}, SAFE)
            screen.delete(0, tk.END)
            screen.insert(0, str(round(result, 10)))
        except Exception:
            screen.delete(0, tk.END)
            screen.insert(0, "Error")
    else:
        screen.insert(tk.END, key)


layout = [
    ["sin(", "cos(", "tan(", "log(", "ln("],
    ["sqrt(", "^", "pi", "e", "fact("],
    ["7", "8", "9", "/", "C"],
    ["4", "5", "6", "*", "DEL"],
    ["1", "2", "3", "-", "("],
    ["0", ".", "=", "+", ")"],
]
for r, row in enumerate(layout, start=1):
    for c, key in enumerate(row):
        color = "#4caf50" if key == "=" else "#ef5350" if key in ("C", "DEL") \
            else "#ffffff" if key.isdigit() or key == "." else "#cfe3f7"
        tk.Button(root, text=key if key == "(" else key.rstrip("("), width=6, height=2, bg=color,
                  font=("Arial", 11, "bold"),
                  command=lambda k=key: press(k)).grid(row=r, column=c, padx=2, pady=2)

root.bind("<Return>", lambda event: press("="))  # Enter key = equals
root.mainloop()
