from tkinter import *

def Scrolled(_widget, _master, _mode='y', **options):
    frame = Frame(_master, bd=2, relief=SUNKEN)
    xscrollbar = yscrollbar = None
    if 'x' in _mode: xscrollbar = Scrollbar(frame, orient=HORIZONTAL)
    if 'y' in _mode: yscrollbar = Scrollbar(frame)
    widget = _widget(frame, **options)
    yscrollbar.grid(row=0, column=1, sticky=N+S)
    widget.grid(row=0, column=0)
    widget.config(yscrollcommand=yscrollbar.set)
    yscrollbar.config(command=widget.yview)
    return widget

def ScrolledCanvas(master, _mode='xy', **options):
    return Scrolled(Canvas, master, _mode, **options)

master = Tk()

widget = ScrolledCanvas(master, "y")

master.mainloop()
