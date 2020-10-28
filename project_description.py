import Tkinter as tk
window = tk.Tk()

header = tk.Frame(master=window, width=600, height=500, bg="white")
header.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

title = tk.Label(master=header, text="Project Description", font=("Helvetica", 26), padx=20, pady=15, bg="white")
title.place(x=0, y=0)

label_1 = tk.Label(text="Project Long Description", font=("Helvetica", 20), padx=20, pady=15, bg="white")
label_1.place(x=0, y=100)

button_2 = tk.Button(text="Exit", font=("Helvetica", 20), padx=20, pady=15, bg="white")
button_2.place(x=400, y=400)

window.mainloop()