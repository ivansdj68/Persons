from tkinter import *
from AddressBook import *
from InfoWindow import *

class AddressBookWindow:

    def __init__(self, master, address_book):
        self.master = master
        window_width = 600
        window_height = 300
        display_x = str(self.master.winfo_screenwidth()//2 - window_width//2)
        display_y = str(self.master.winfo_screenheight()//2 - window_height//2)
        self.master.geometry(str(window_width) + 'x' + str(window_height) + '+' + display_x + '+' + display_y)
        self.master.config(bg="black")

        self.adBook = address_book

        self.buttons = [Button(self.master, text="Add", bg=self.master.cget("bg"), fg="white"),
                        Button(self.master, text="Sort", bg=self.master.cget("bg"), fg="white"),
                        Button(self.master, text="Search", bg=self.master.cget("bg"), fg="white")]
        self.buttons[2].place(x=130, y=0)
        self.buttons[0].place(x=200, y=0)
        self.buttons[1].place(x=240, y=0)

        self.search_entry = Entry(self.master,
                                  textvariable="search",
                                  highlightcolor="blue",
                                  highlightbackground="gray",
                                  highlightthickness=1)
        self.search_entry.bind("<Return>", self.searchEvent)
        self.search_entry.place(x=1, y=1)
        self.search_entry.focus_set()

        self.draw_widgets()

        self.prev_IW_contact = None

        self.clicked = None

    def draw_names(self):
        y = 60
        names = self.adBook.get_address_book_names()
        for c in range(len(names)):
            button = Button(self.master,
                            text=names[c],
                            relief=FLAT,
                            bg=self.master.cget("bg"),
                            fg="white")
            # Draws button with contact name
            button.bind("<Button-1>", func=self.showInfoEvent)
            button.place(x=0, y=y)
            y += 30

    def assign_option_events(self):
        for b in range(len(self.buttons)):
            current_button = self.buttons[b]
            current_button.bind("<Button-1>", func=self.optionEventSelector(b))

    def draw_widgets(self):
        self.draw_names()
        self.assign_option_events()

    def showInfoEvent(self, event):
        self.clicked = event.widget
        contact_name = event.widget.cget("text")  # Gets the name of the clicked contact
        if self.prev_IW_contact is not contact_name:
            self.prev_IW_contact = contact_name
            InfoWindow(self.master, self.adBook, self, contact_name)

    def get_clicked_widget(self):
        return self.clicked

    def optionEventSelector(self, num):
        if num == 0:
            return self.addContactEvent
        elif num == 1:
            return self.sortContactsEvent
        elif num == 2:
            return self.searchEvent

    def addContactEvent(self, event):
        InfoWindow(self.master, self.adBook, self, "new")

    def sortContactsEvent(self, event):
        #self.adBook.sort()
        print("Sort")

    def searchEvent(self, event):
        contact_name = self.search_entry.get()
        if self.prev_IW_contact is not contact_name:
            self.prev_IW_contact = contact_name
            InfoWindow(self.master, self.adBook, contact_name)

root = Tk()
#root.withdraw Withdraw this widget from the screen such that it is unmapped and forgotten by the window manager. Re-draw it with wm_deiconify.

ab = AddressBook()
AddressBookWindow(root, ab)
root.mainloop()
