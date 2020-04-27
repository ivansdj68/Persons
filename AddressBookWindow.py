from tkinter import *

class AddressBookWindow:

    def __init__(self, master):
        #self.ad_book = ad_book
        self.master = master
        self.master.title("GUI")
        self.buttons = ["add", "delete", "edit", "sort", "search"]
        self.searchEntry = "searchBar"
        self.label = Label(self.master, text="Hello there.")
        self.label.pack()

root = Tk()
gui = AddressBookWindow(root)
root.mainloop()
