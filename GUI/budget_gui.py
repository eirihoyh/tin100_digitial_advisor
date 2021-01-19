import tkinter as tk
from tkinter import ttk

from backend_code.person import Student, Family, Retired
from backend_code.database_connecter import StoreInDatabase


# -------Functions-------------
def increase():
    """
    Increases number of people
    """
    value = int(label_members["text"])
    if value < 10:
        label_members["text"] = f"{value + 1}"


def decrease():
    """
    Decreases number of people
    """
    value = int(label_members["text"])
    if value > 1:
        label_members["text"] = f"{value - 1}"


person = []  # Need to save the person outside the function


def calc_budget():
    """
    A function that calculates an estimation for budget using superclass Person
    """
    status = my_combo.get()
    nr_of_people = int(label_members["text"])
    avrg_income = income_entry.get()
    debt = loan_entry.get()

    if status == "Student":
        person.append(Student(nr_of_people, avrg_income, debt))

    elif status == "Family":
        person.append(Family(nr_of_people, avrg_income, debt))
    else:
        person.append(Retired(nr_of_people, avrg_income, debt))

    suggest_budget = person[-1].calculate_budget()

    for key in budget_setup:
        budget_setup[key].delete(0, tk.END)
        budget_setup[key].insert(0, round(float(suggest_budget[key]), 2))


def save_info():
    """
    function for save button that saves the budget
    :return:
    """
    money = []
    for key in budget_setup:
        money.append(round(float(budget_setup[key].get()), 2))

    if not person[-1].check_budget(sum(money)):
        approval_label["text"] = "Must not go beyond budget"
    else:
        save = StoreInDatabase()
        save.insert_data(money[0], money[1], money[2], money[3], money[4], money[5])
        approval_label["text"] = "Saved!"


# -------standard dictionaries----------

wanted_information = {
    "Status:": ["Student", "Family", "Retired"],
    "Nr. of people:": 1,
    "Average monthly income:": 0,
    "Monthly debt payment:": 0
}

budget_setup = {
    "Food/drinks": 0,
    "Clothing": 0,
    "Travel": 0,
    "Payments": 0,
    "Buffer account": 0,
    "Freetime": 0
}

# -----------GUI begins----------------
root = tk.Tk()
root.title("Information about user")

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

# ----------first question: Status---------------

label0 = tk.Label(master=frame0, text=f"{keys[0]}")
label0.grid(row=0, column=1, sticky="e")

clicked = tk.StringVar(0)
clicked.set(wanted_information[keys[0]])

my_combo = ttk.Combobox(frame0, value=wanted_information[keys[0]])
my_combo.current(0)
my_combo.bind("<<ComboboxSelected>>")
my_combo.grid(row=0, column=1, sticky="w")

# ----------second question: Nr of people------------

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

# ---------third question: Salary-------------

income_entry = tk.Entry(master=frame0)
income_entry.grid(row=2, column=1)

kr_label1 = tk.Label(master=frame0, text="Kr")
kr_label1.grid(row=2, column=2, sticky='w')

# --------fourth question: Amount of loan----------------

loan_entry = tk.Entry(master=frame0)
loan_entry.grid(row=3, column=1)

kr_label2 = tk.Label(master=frame0, text="Kr")
kr_label2.grid(row=3, column=2, sticky='w')

# ----------calculation buttons---------------------


calc_frame = tk.Frame(master=root, borderwidth=5)
calc_frame.grid(row=1, column=0)

calc_button = tk.Button(master=calc_frame, text="Calculate budget",
                        relief=tk.RAISED, borderwidth=5, command=calc_budget)
calc_button.pack()

# ---------------budget part----------------------


budget_frame = tk.Frame(master=root, width=100, height=100, borderwidth=5, relief=tk.SUNKEN)
budget_frame.grid(row=3, column=0)

for index, info in enumerate(budget_setup.keys()):
    budget_frame.rowconfigure(index, minsize=25, weight=1)
    budget_frame.columnconfigure([0, 1, 2], minsize=100, weight=1)

    label = tk.Label(master=budget_frame, text=info)
    label.grid(row=index, column=0, sticky="e", padx=10, pady=10)

    budget_setup[info] = tk.Entry(master=budget_frame, width=50, text=f"{info}")
    budget_setup[info].grid(row=index, column=1, sticky="ew", padx=10, pady=10)

    kr_label = tk.Label(master=budget_frame, text="Kr")
    kr_label.grid(row=index, column=2, sticky='w')

# ----------save button--------------------

last_frame = tk.Frame(master=root, borderwidth=5)
last_frame.grid(row=4, column=0)

last_frame.columnconfigure(0, minsize=500)
last_frame.rowconfigure(0, minsize=25)

approval_label = tk.Label(master=last_frame, text="")
approval_label.grid(row=0, column=0, sticky="ew")

save_button = tk.Button(master=last_frame, text="Save", relief=tk.RAISED,
                        borderwidth=5, command=save_info)
save_button.grid(row=0, column=1, sticky="e", padx=5, pady=5)

root.mainloop()
