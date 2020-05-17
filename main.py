from AddressBook import *
from AddressBookWindow import *
from tkinter import *

root = Tk()
ab = AddressBook()
abw = AddressBookWindow(root,ab)

root.mainloop()
