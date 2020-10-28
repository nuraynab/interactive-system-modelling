import Tkinter as tk
window = tk.Tk()

header = tk.Frame(master=window, width=600, height=400, bg="white")
header.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

title = tk.Label(master=header, text="Delete Project", font=("Helvetica", 26), padx=20, pady=15, bg="white")
title.place(x=0, y=0)

label_1 = tk.Label(text="Are you sure you want to delete this project\n and its versions?", font=("Helvetica", 20), padx=20, pady=15, bg="white")
label_1.place(x=0, y=100)

button_1 = tk.Button(text="Delete", font=("Helvetica", 20), padx=20, pady=15, bg="white")
button_1.place(x=100, y=250)

button_2 = tk.Button(text="Cancel", font=("Helvetica", 20), padx=20, pady=15, bg="white")
button_2.place(x=340, y=250)

window.mainloop()