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

frame0 = tk.Frame(master=root, borderwidth=5, relief=tk.SUNKEN)
frame0.grid(row=0, column=0)

keys = []
for key in wanted_information.keys():
    keys.append(key)

for index, info in enumerate(wanted_information.keys()):
    frame0.rowconfigure(index, minsize=25)
    frame0.columnconfigure([0, 1], minsize=100)

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

income_entry = tk.Entry(master=frame0, text=f"{wanted_information[keys[2]]}",
                        cursor="arrow", exportselection=0)
income_entry.grid(row=2, column=1)

# --------fourth question----------------

income_entry = tk.Entry(master=frame0, text=f"{wanted_information[keys[3]]}",
                        cursor="arrow", exportselection=0)
income_entry.grid(row=3, column=1)

# ---------------calculation buttons---------------

calc_frame = tk.Frame(master=root, borderwidth=5)
calc_frame.grid(row=1, column=0)

calc_button = tk.Button(master=calc_frame, text="Calculate budget",
                        relief=tk.RAISED, borderwidth=5)
calc_button.pack()

root.mainloop()