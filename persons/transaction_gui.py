import tkinter as tk

root = tk.Tk()

root.title("Pop up when registered transaction")

frame0 = tk.Frame(master=root, width=100, height=100, borderwidth=5, relief=tk.SUNKEN)
frame0.grid(row=0, column=0)

frame0.rowconfigure(0, minsize=25, weight=1)
frame0.columnconfigure([0, 1, 2], minsize=100, weight=1)

label = tk.Label(master=frame0, text="Transaction amount:", bg="white")
label.grid(row=0, column=0, sticky="e", padx=10, pady=10)

entry = tk.Entry(master=frame0)
entry.grid(row=0,column=1, sticky="ew", padx=10, pady=10)

button = tk.Button(master=frame0, text="Make transaction")
button.grid(row=0, column=2, sticky="nsew", padx=10, pady=10)

frame1 = tk.Frame(master=root, width=100, height=100, borderwidth=5)
frame1.grid(row=1, column=0)

message = tk.Label(master=frame1, text="Welcome!")
message.pack()

root.mainloop()