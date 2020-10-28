import Tkinter as tk
window = tk.Tk()

header = tk.Frame(master=window, width=600, height=600, bg="white")
header.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

title = tk.Label(master=header, text="Save Version", font=("Helvetica", 26), padx=20, pady=15, bg="white")
title.place(x=0, y=0)

label_1 = tk.Label(text="Do you want to save the changes\n as the current version or as a new version?", font=("Helvetica", 20), padx=20, pady=15, bg="white")
label_1.place(x=0, y=100)

check_1 = tk.Checkbutton(text="Current", font=("Helvetica", 20), bg="white")
check_1.place(x=80, y=200)

check_2 = tk.Checkbutton(text="New", font=("Helvetica", 20), bg="white")
check_2.place(x=350, y=200)

label_2 = tk.Label(text="The changes are major or minor?", font=("Helvetica", 20), padx=20, pady=15, bg="white")
label_2.place(x=0, y=250)

check_1 = tk.Checkbutton(text="Major", font=("Helvetica", 20), bg="white")
check_1.place(x=80, y=350)

check_2 = tk.Checkbutton(text="Minor", font=("Helvetica", 20), bg="white")
check_2.place(x=350, y=350)


button_1 = tk.Button(text="Save", font=("Helvetica", 20), padx=20, pady=15, bg="white")
button_1.place(x=100, y=450)

button_2 = tk.Button(text="Cancel", font=("Helvetica", 20), padx=20, pady=15, bg="white")
button_2.place(x=340, y=450)

window.mainloop()