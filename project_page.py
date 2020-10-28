from Tkinter import *
window = Tk()
c = Canvas(window, width=1900, height=1000, bg="white")
c.pack()

header = Frame(master=window, width=1500, height=1000, bg="white")
header.pack(fill=BOTH, side=LEFT, expand=True)

title = Label(master=window, text="Project: Animal-Dog", font=("Helvetica", 26), padx=20, pady=15, bg="white")
title.place(x=0, y=0)

button_0_1 = Button(text="Edit Database", font=("Helvetica", 20), padx=20, pady=15, bg="white")
button_0_1.place(x=500, y=10)
button_0_2 = Button(text="Run", font=("Helvetica", 20), padx=20, pady=15, bg="white")
button_0_2.place(x=780, y=10)
button_0_3 = Button(text="Save Version", font=("Helvetica", 20), padx=20, pady=15, bg="white")
button_0_3.place(x=900, y=10)
button_0_4 = Button(text="Exit Version", font=("Helvetica", 20), padx=20, pady=15, bg="white")
button_0_4.place(x=1160, y=10)

label_1 = Label(text="Version 1.1: New", font=("Helvetica", 20), padx=20, pady=15, bg="white")
label_1.place(x=0, y=100)

button_1 = Button(text="Experiments", font=("Helvetica", 20), padx=20, pady=15, bg="white")
button_1.place(x=450, y=200)

button_2 = Button(text="Environment", font=("Helvetica", 20), padx=20, pady=15, bg="white")
button_2.place(x=850, y=200)

c.create_rectangle(100,290,1300,900)

label_2 = Label(text="Human Memory", font=("Helvetica", 20), padx=20, pady=15, bg="white")
label_2.place(x=500, y=300)

button_3 = Button(text="Sensory Memory", font=("Helvetica", 20), padx=20, pady=15, bg="white")
button_3.place(x=900, y=400)

button_4 = Button(text="Short-Term Memory", font=("Helvetica", 20), padx=20, pady=15, bg="white")
button_4.place(x=900, y=650)

c.create_rectangle(120,380,850,880)

label_3 = Label(text="Long-Term Memory", font=("Helvetica", 20), padx=20, pady=15, bg="white")
label_3.place(x=300, y=400)

button_5 = Button(text="Procedural Memory", font=("Helvetica", 20), padx=20, pady=15, bg="white")
button_5.place(x=530, y=480)

c.create_rectangle(140,470,520,860)

label_4 = Label(text="Declarative Memory", font=("Helvetica", 20), padx=20, pady=15, bg="white")
label_4.place(x=160, y=480)

button_6 = Button(text="Episodic Memory", font=("Helvetica", 20), padx=20, pady=15, bg="white")
button_6.place(x=170, y=600)

button_7 = Button(text="Semantic Memory", font=("Helvetica", 20), padx=20, pady=15, bg="white")
button_7.place(x=160, y=700)


window.mainloop()