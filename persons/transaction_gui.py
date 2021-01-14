import tkinter as tk
from tkinter import ttk

from look_at_transactions import Transaction


def make_transaction():
    transaction = Transaction(clicked.get())
    message["text"] = f"{transaction.transaction_type}"


root = tk.Tk()

root.title("Pop up when registered transaction")

frame0 = tk.Frame(master=root, width=100, height=100, borderwidth=5, relief=tk.SUNKEN)
frame0.grid(row=0, column=0)

frame0.rowconfigure(0, minsize=25, weight=1)
frame0.columnconfigure([0, 1], minsize=50, weight=1)

transaction_types = ["Food", "Travel", "Payments"]

clicked = tk.StringVar(0)
clicked.set(transaction_types[0])

my_combo = ttk.Combobox(frame0, value=transaction_types)
my_combo.current(0)
my_combo.bind("<<ComboboxSelected>>")
my_combo.grid(row=0, column=0, sticky="e", padx=10, pady=10)

button = tk.Button(master=frame0, text="Make transaction", command=make_transaction)
button.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

frame1 = tk.Frame(master=root, width=100, height=100, borderwidth=5)
frame1.grid(row=1, column=0)

message = tk.Label(master=frame1, text="Welcome!")
message.pack()

root.mainloop()
