# Authors:
#
# Name:                     Student ID:
# Amanda Burgos De Jesus    #97280
# Hiram Zengotita Hernandez #103450
# Ivan Santiago De Jesus    #85519
#

from AddressBook import *
from AddressBookWindow import *
from tkinter import *

root = Tk()
ab = AddressBook()
abw = AddressBookWindow(root,ab)

root.mainloop()
