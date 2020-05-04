from tkinter import *
from Contact import *
from AddressBook import *
from AddressBookWindow import *

root = Tk()
c1 = Contact("Amanda", "787-456")
c2 = Contact("Hiram", "787-789", "email@domain.com")
c3 = Contact("Ivan", "787-123")
aBook = [c3, c2, c1]
abObj = AddressBook(aBook)
gui = AddressBookWindow(root, abObj)
root.mainloop()
