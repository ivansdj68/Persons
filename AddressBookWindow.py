from tkinter import *
from AddressBook import *

class AddressBookWindow:

    def __init__(self, master, address_book):
        self.master = master
        self.adBook = address_book
        self.buttons = [Button(self.master, text="Add"), Button(self.master, text="Delete"),
                        Button(self.master, text="Edit"), Button(self.master, text="Sort"),
                        Button(self.master, text="Search")]
        self.search_entry = Entry(self.master, text="Search Contact")
        self.draw_widgets()

    def draw_names(self):
        y = 30
        for c in range(self.adBook.getSize()):
            contact_name = self.adBook.getContactByIndex(c).getName()
            button = Button(self.master, text=contact_name)
            button.bind("<Button-1>", func=self.showInfoEvent)
            button.place(x=0, y=y)
            y += 30

    def draw_options(self):
        x = 0
        for b in range(len(self.buttons)):
            current_button = self.buttons[b]
            current_button.bind("<Button-1>", func=self.optionEventSelector(b))
            current_button.place(x=x, y=275)
            x += 50

    def draw_search_entry(self):
        self.search_entry.place(x=90, y=0)

    def draw_widgets(self):
        self.draw_names()
        self.draw_options()
        self.draw_search_entry()

    def showInfoEvent(self, event):
        contact_name = event.widget.cget("text")
        contact_obj = self.adBook.getContactByName(contact_name)
        contact_obj.showInfo()

    def optionEventSelector(self, num):
        if num == 0:
            return self.addContactEvent
        elif num == 1:
            return self.deleteContactEvent
        elif num == 2:
            return self.editContactEvent
        elif num == 3:
            return self.sortContactsEvent
        elif num == 4:
            return self.searchEvent

    def addContactEvent(self, event):
        #self.adBook.addContact()
        print("Add")

    def deleteContactEvent(self, event):
        #self.adBook.deleteContact()
        print("Delete")

    def editContactEvent(self, event):
        #self.adBook.editContact()
        print("Edit")

    def sortContactsEvent(self, event):
        #self.adBook.sort()
        print("Sort")

    def searchEvent(self, event):
        contact_info = self.search_entry.get()
        contact = self.adBook.getContact(contact_info)
        try:
            contact.showInfo()
        except AttributeError:
            print("Invalid search criteria or contact does not exist")
            pass
        print("Search")
