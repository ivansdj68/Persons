from tkinter import *
from AddressBook import *
from InfoWindow import *

class AddressBookWindow:

    def __init__(self, master, address_book):
        self.master = master
        window_width = 300*2
        window_height = 300*2
        display_x = str(self.master.winfo_screenwidth()//2 - window_width//2)
        display_y = str(self.master.winfo_screenheight()//2 - window_height//2)
        self.master.geometry(str(window_width) + 'x' + str(window_height) + '+' + display_x + '+' + display_y)
        self.ABWFrame = Frame(master=self.master, height=0, width=window_width//2)
        self.IWFrame = Frame(master=self.master, height=window_height//2, width=window_width)
        self.ABWFrame.place(x=0, y=0)
        self.IWFrame.place(x=300, y=0)
        self.adBook = address_book
        self.buttons = [Button(self.master, text="Add"), Button(self.master, text="Sort"),
                        Button(self.master, text="Search")]
        self.search_entry = Entry(self.master, text="Search Contact")
        self.search_entry.bind("<Return>", self.searchEvent)
        self.draw_widgets()

    def draw_names(self):
        y = 30
        names = self.adBook.get_address_book_names()
        for c in range(self.adBook.get_size()):
            button = Button(self.master, text=names[c], relief=GROOVE)  # Draws button with contact name
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
        self.buttons[2].place(x=220, y=0)
        self.search_entry.place(x=90, y=0)

    def draw_widgets(self):
        self.draw_names()
        self.draw_options()
        self.draw_search_entry()

    def showInfoEvent(self, event):
        contact_name = event.widget.cget("text")  # Gets the first name of the contact
        InfoWindow(self.IWFrame, self.adBook, contact_name)

    def optionEventSelector(self, num):
        if num == 0:
            return self.addContactEvent
        elif num == 1:
            return self.sortContactsEvent
        elif num == 2:
            return self.searchEvent

    def addContactEvent(self, event):
        InfoWindow(self.IWFrame, self.adBook, None)

    def sortContactsEvent(self, event):
        #self.adBook.sort()
        print("Sort")

    def searchEvent(self, event):
        contact_name = self.search_entry.get()
        contacts = self.adBook.searchList(contact_name)  # List with contacts that match\
        try:
            contacts.showInfo()
        except AttributeError:
            print("Invalid search criteria or contact does not exist")

root = Tk()
#root.withdraw Withdraw this widget from the screen such that it is unmapped and forgotten by the window manager. Re-draw it with wm_deiconify.

ab = AddressBook()
AddressBookWindow(root, ab)
root.mainloop()
