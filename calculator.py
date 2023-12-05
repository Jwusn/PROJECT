import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def clear_entry():
    entry.delete(0, tk.END)

def clear_last_entry():
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text[:-1])

def insert_key(key):
    if key.isdigit() or key in ['+', '-', '*', '/', '.', 'Return']:
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current_text + key)
    elif key == '\x08':
        clear_last_entry()

root = tk.Tk()
root.title("Simple Calculator")

# Increase the size of the entry field
entry = tk.Entry(root, width=16, font=("Arial", 20), borderwidth=5, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Create buttons for digits and operations with larger font
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C', 'CE'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        tk.Button(root, text=button, font=("Arial", 20), command=calculate, padx=20, pady=20).grid(row=row_val, column=col_val, sticky="nsew")
    elif button == 'C':
        tk.Button(root, text=button, font=("Arial", 20), command=clear_entry, padx=20, pady=20).grid(row=row_val, column=col_val, sticky="nsew")
    elif button == 'CE':
        tk.Button(root, text=button, font=("Arial", 20), command=clear_last_entry, padx=20, pady=20).grid(row=row_val, column=col_val, sticky="nsew")
    else:
        tk.Button(root, text=button, font=("Arial", 20), command=lambda b=button: insert_key(b), padx=20, pady=20).grid(row=row_val, column=col_val, sticky="nsew")
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Configure row and column weights to make the buttons fill the window
for i in range(1, 5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Set a minimum size for the window
root.update_idletasks()
root.minsize(root.winfo_reqwidth(), root.winfo_reqheight())

# Center the window on the screen
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
x = (width - root.winfo_reqwidth()) // 2
y = (height - root.winfo_reqheight()) // 2
root.geometry("+{}+{}".format(x, y))

# Enable keyboard input
root.bind('<Key>', lambda event: insert_key(event.char))
# Bind Enter key to calculate
root.bind('<Return>', lambda event: calculate())

root.mainloop()