# import tkinter as tk
#
# class Application(tk.Frame):
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.geometry("300x200")
#
#         tk.Frame.__init__(self, self.root)
#         self.create_widgets()
#
#     def create_widgets(self):
#         self.root.bind('<Return>', self.parse)
#         self.grid()
#
#         submit = tk.Button(self, text="Submit")
#         submit.bind('<Button-1>', self.parse)
#         submit.grid()
#
#     def parse(self, event):
#         print("You clicked?")
#
#     def start(self):
#         self.root.mainloop()
#
#
# Application().start()



# from tkinter import *
#
# root = Tk()
#
# def callback(event):
#     print("clicked at", event.x, event.y)
#
# frame = Frame(root, width=100, height=100)
# frame.bind("<Button-1>", callback)
# frame.pack()
#
# root.mainloop()

# from tkinter import *
#
# root = Tk()
#
# def key(event):
#     print("pressed", repr(event.char))
#
# def callback(event):
#     frame.focus_set()
#     print("clicked at", event.x, event.y)
#     print(event.widget)
#     print(event.widget.winfo_width())
#
# frame = Frame(root, width=100, height=100)
# frame.bind("<Key>", key)
# frame.bind("<Button-1>", callback)
# frame.pack()
#
# root.mainloop()
