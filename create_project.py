import Tkinter as tk
window = tk.Tk()

header = tk.Frame(master=window, width=600, height=1000, bg="white")
header.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

title = tk.Label(master=header, text="Edit Project Information", font=("Helvetica", 26), padx=20, pady=15, bg="white")
title.place(x=0, y=0)

label_1 = tk.Label(text="Project Name", font=("Helvetica", 20), padx=20, pady=15, bg="white")
label_1.place(x=0, y=100)
entry_1 = tk.Entry()
entry_1.place(x=250, y=110, width=250, height=50)

label_2 = tk.Label(text="Short Description", font=("Helvetica", 20), padx=20, pady=15, bg="white")
label_2.place(x=0, y=160)
entry_2 = tk.Entry()
entry_2.place(x=20, y=230, width=480, height=150)

label_3 = tk.Label(text="Long Description", font=("Helvetica", 20), padx=20, pady=15, bg="white")
label_3.place(x=0, y=390)
label_3_1 = tk.Label(text="Optional", font=("Helvetica", 14), padx=20, pady=5, bg="white", fg="gray")
label_3_1.place(x=0, y=440)
entry_3 = tk.Entry()
entry_3.place(x=20, y=480, width=480, height=250)

button_1 = tk.Button(text="Save", font=("Helvetica", 20), padx=20, pady=15, bg="white")
button_1.place(x=60, y=760)

button_2 = tk.Button(text="Cancel", font=("Helvetica", 20), padx=20, pady=15, bg="white")
button_2.place(x=300, y=760)

window.mainloop()