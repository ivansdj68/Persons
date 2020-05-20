from tkinter import *

root = Tk()
root.geometry("600x300+400+300")

frame = Frame(root, bd=2, relief=SUNKEN)

frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

yscrollbar = Scrollbar(frame)
yscrollbar.grid(row=0, column=1, sticky=N+S)

canvas = Canvas(frame, bd=0, scrollregion=(0, 0, 0, 700),
                yscrollcommand=yscrollbar.set)

canvas.grid(row=0, column=0, sticky=N+S)

yscrollbar.config(command=canvas.yview)

for i in range(20):
    button = Button(canvas, text=str(i))
    button.grid(row=i, column=0)

frame.pack()

root.mainloop()