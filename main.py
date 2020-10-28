from Tkinter import *
import tkMessageBox 

def close_window(): 
    window.destroy()

def delete_project():
	answer = tkMessageBox.askokcancel(title="Delete Project", message="Are you sure you want to delete this project and its versions?")

def delete_version():
	answer = tkMessageBox.askokcancel(title="Delete Version", message="Are you sure you want to delete this version?")


window = Tk()

header = Frame(master=window, highlightbackground="grey", highlightthickness=1, width=1200, height=100, bg="white")
header.pack(side=TOP, fill=X, expand=1, anchor=N)

title = Label(master=header, text="Interactive System Modeling", font=("Helvetica", 32), padx=20, pady=15, bg="white")
title.pack(side=LEFT)

exitBtn = Button(master=header, text="Exit", width=10, height=2, command = close_window)
exitBtn.pack(side=RIGHT)


createBtn = Button(master=header, text="Create a project", width=15, height=2)
createBtn.pack(side=RIGHT)


body = Frame(master=window, highlightbackground="grey", highlightthickness=1, width=1200, height=700, bg="white")
body.pack(side=BOTTOM, fill=BOTH, expand=1, anchor=S)


Label(master=body, text="Projects", font=("Helvetica", 20), padx=20, pady=15, bg="white").place(x=200, y=20)

projects = Listbox(master=body, width=30, height=10)
projects.place(x=120, y=75)
projects.insert(0, "Project1")

Button(master=body, text="Edit Info", width=10, height=2).place(x=120, y=300)
Button(master=body, text="Delete", width=10, height=2, command = delete_project).place(x=318, y=300)

Label(master=body, text="Project Description", font=("Helvetica", 20), padx=20, pady=5, bg="white").place(x=140, y=400)
Label(master=body, text="Project Short Description", font=("Helvetica", 14), padx=20, pady=5, bg="white").place(x=90, y=450)
Button(master=body, text="Project Long Description", width=30, height=2).place(x=110, y=500)

Label(master=body, text="Versions", font=("Helvetica", 20), padx=20, pady=15, bg="white").place(x=800, y=20)

versions = Listbox(master=body, width=30, height=10)
versions.place(x=720, y=75)
versions.insert(0, "Version1")

Button(master=body, text="Edit Info", width=10, height=2).place(x=720, y=300)
Button(master=body, text="Delete", width=10, height=2, command = delete_version).place(x=918, y=300)

Label(master=body, text="Version Description", font=("Helvetica", 20), padx=20, pady=5, bg="white").place(x=740, y=400)
Label(master=body, text="Version Short Description", font=("Helvetica", 14), padx=20, pady=5, bg="white").place(x=690, y=450)
Button(master=body, text="Version Long Description", width=30, height=2).place(x=710, y=500)


Button(master=body, text="Open", width=10, height=2).place(x=1000, y=600)

window.mainloop()