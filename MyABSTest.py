from tkinter import *
from AutoScrollbar import *

master = Tk()

scrollbar = AutoScrollbar(master)
scrollbar.grid(row=0, column=1, sticky=N+S)

canvas = Canvas(master, yscrollcommand=scrollbar.set)
canvas.grid(row=0, column=0, sticky=N+S+E+W)

scrollbar.config(command=canvas.yview)

# make the canvas expandable
master.grid_rowconfigure(0, weight=1)

# create canvas contents
frame = Frame(canvas, width=50, height=300)
frame.rowconfigure(1, weight=1)

rows = 5
for i in range(1, rows):
    for j in range(1, 10):
        button = Button(frame, padx=7, pady=7, text="[%d,%d]" % (i,j))
        button.grid(row=i, column=j, sticky='news')

canvas.create_window(0, 0, anchor=NW, window=frame)

frame.update_idletasks()

canvas.config(scrollregion=canvas.bbox("all"))

canvas.focus_set()

master.mainloop()
