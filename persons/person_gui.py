import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Information about user")

wanted_information = {
    "Status:": ["Student", "Family", "Retired"],
    "Nr. of people:": 1,
    "Average monthly income:": 0,
    "Monthly debt payment:": 0
}

frame0 = tk.Frame(master=root, width=100, height=100, borderwidth=5, relief=tk.SUNKEN)
frame0.grid(row=0, column=0)

keys = []
for key in wanted_information.keys():
    keys.append(key)

for index, info in enumerate(wanted_information.keys()):
    frame0.rowconfigure(index, minsize=25, weight=1)
    frame0.columnconfigure([0, 1], minsize=100, weight=1)

    label = tk.Label(master=frame0, text=info)
    label.grid(row=index, column=0, sticky="e", padx=10, pady=10)

# ----------first question---------------

label0 = tk.Label(master=frame0, text=f"{keys[0]}")
label0.grid(row=0, column=1, sticky="e")

clicked = tk.StringVar(0)
clicked.set(wanted_information[keys[0]])

my_combo = ttk.Combobox(frame0, value=wanted_information[keys[0]])
my_combo.current(0)
my_combo.bind("<<ComboboxSelected>>")
my_combo.grid(row=0, column=1, sticky="w")


# ----------second question------------

def increase():
    value = int(label_members["text"])
    if value < 10:
        label_members["text"] = f"{value + 1}"


def decrease():
    value = int(label_members["text"])
    if value > 1:
        label_members["text"] = f"{value - 1}"


label_members = tk.Label(master=frame0, text=f"{wanted_information[keys[1]]}", bg="white")
label_members.grid(row=1, column=1, sticky="ew")

frame1 = tk.Frame(master=frame0)
frame1.grid(row=1, column=2)

frame1.rowconfigure([0, 1], minsize=10)
frame1.columnconfigure(0, minsize=30)

pluss_button = tk.Button(master=frame1, text="+", command=increase)
pluss_button.grid(row=0, column=0, sticky="nsew")

minus_button = tk.Button(master=frame1, text="-", command=decrease)
minus_button.grid(row=1, column=0, sticky="nsew")

# ---------third question-------------

income_entry = tk.Entry(master=frame0)
income_entry.grid(row=2, column=1)

kr_label1 = tk.Label(master=frame0, text="Kr")
kr_label1.grid(row=2, column=2, sticky='w')

# --------fourth question----------------

loan_entry = tk.Entry(master=frame0)
loan_entry.grid(row=3, column=1)

kr_label2 = tk.Label(master=frame0, text="Kr")
kr_label2.grid(row=3, column=2, sticky='w')

# ---------------calculation buttons---------------

calc_frame = tk.Frame(master=root, borderwidth=5)
calc_frame.grid(row=1, column=0)

calc_button = tk.Button(master=calc_frame, text="Calculate budget",
                        relief=tk.RAISED, borderwidth=5)
calc_button.pack()

# ---------------budget part----------------------

# budget_setup burde bli hentet fra classen, ikek skrives inn manuelt
budget_setup = {
    "Food/drinks": 0,
    "Clothing": 0,
    "Travel": 0,
    "Payments": 0,
    "Buffer account": 0,
    "Freetime": 0
}

budget_frame = tk.Frame(master=root, width=100, height=100, borderwidth=5, relief=tk.SUNKEN)
budget_frame.grid(row=3, column=0)

for index, info in enumerate(budget_setup.keys()):
    budget_frame.rowconfigure(index, minsize=25, weight=1)
    budget_frame.columnconfigure([0, 1, 2], minsize=100, weight=1)

    label = tk.Label(master=budget_frame, text=info)
    label.grid(row=index, column=0, sticky="e", padx=10, pady=10)

    entry = tk.Entry(master=budget_frame, width=50)
    entry.grid(row=index, column=1, sticky="ew", padx=10, pady=10)

    kr_label = tk.Label(master=budget_frame, text="Kr")
    kr_label.grid(row=index, column=2, sticky='w')

# ----------save button--------------------

last_frame = tk.Frame(master=root, borderwidth=5)
last_frame.grid(row=4, column=0)

last_frame.columnconfigure(0, minsize=500)
last_frame.rowconfigure(0, minsize=25)

save_button = tk.Button(master=last_frame, text="Save", relief=tk.RAISED, borderwidth=5)
save_button.grid(row=0, column=0, sticky="e", padx=5, pady=5)

root.mainloop()
