import Tkinter as tk
window = tk.Tk()

header = tk.Frame(master=window, width=600, height=400, bg="white")
header.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

title = tk.Label(master=header, text="Exit Version", font=("Helvetica", 26), padx=20, pady=15, bg="white")
title.place(x=0, y=0)

label_1 = tk.Label(text="Do you want to save the changes?", font=("Helvetica", 20), padx=20, pady=15, bg="white")
label_1.place(x=0, y=100)

button_1 = tk.Button(text="Yes", font=("Helvetica", 20), padx=20, pady=15, bg="white")
button_1.place(x=50, y=250)

button_2 = tk.Button(text="Delete", font=("Helvetica", 20), padx=20, pady=15, bg="white")
button_2.place(x=200, y=250)

button_3 = tk.Button(text="Cancel", font=("Helvetica", 20), padx=20, pady=15, bg="white")
button_3.place(x=380, y=250)

window.mainloop()