from tkinter import *
from AddressBook import *
from InfoWindow import *

class AddressBookWindow:
    """A window to access an address book's contacts."""

    def __init__(self, master, address_book):
        """Receives a tkinter root and AddressBook instance."""
        self.master = master
        self.master.title("Persons")
        self.master.resizable(False, False)
        window_width = 600
        window_height = 300
        display_x = str(self.master.winfo_screenwidth()//2 - window_width//2)
        display_y = str(self.master.winfo_screenheight()//2 - window_height//2)
        self.master.geometry(str(window_width) + 'x' + str(window_height) + '+' + display_x + '+' + display_y)
        self.master.config(bg="black")

        self.frame_contacts = Frame(self.master, width=150, height=240, bg="black")

        self.address_book = address_book

        self.button_list = []

        self.add_button = Button(self.master, text="Add", bg=self.master.cget("bg"), fg="white", command=self.add_contact_event)
        self.search_button = Button(self.master, text="Search", bg=self.master.cget("bg"), fg="white")
        self.add_button.place(x=200, y=0)
        self.search_button.place(x=130, y=0)

        self.search_entry = Entry(self.master,
                                  textvariable="search",
                                  highlightcolor="blue",
                                  highlightbackground="gray",
                                  highlightthickness=1)
        self.search_entry.bind("<Key>", func=self.entry_matches)
        self.search_entry.bind("<Return>", func=self.search_event)
        self.search_button.bind("<Button-1>", func=self.search_event)
        self.search_entry.place(x=1, y=1)
        self.search_entry.focus_set()
        
        self.frame_search = Frame(self.master, width=126, height=100, bg="gray")

        self.first = True

        self.prev_IW_contact = None

        self.draw_names()

    def draw_names(self):
        """Makes names list with buttons to access each contact's info."""
        if self.first==False:
           self.remove_contact_buttons()
        self.first = False
        self.frame_contacts.place(x=0, y=60)
        names = self.address_book.get_names()
        for c in names:
            # Draws button with contact name
            button = Button(self.frame_contacts,
                            text=c,
                            relief=FLAT,
                            bg=self.master.cget("bg"),
                            fg="white")
            button.bind("<Button-1>", func=self.show_info_event)
            button.pack()

    def remove_contact_buttons(self):
        copy_frame = Frame(self.master, width=150, height=240, bg="black")
        self.frame_contacts.destroy()
        self.frame_contacts = copy_frame

    def show_info_event(self, event):
        """Signals the contact to be shown in InfoWindow."""
        self.frame_search.place_forget()
        contact_name = event.widget.cget("text")  # Gets the name of the clicked contact
        if self.prev_IW_contact is not contact_name:
            self.prev_IW_contact = contact_name
            InfoWindow(self.master, self.address_book, self, contact_name)

    def add_contact_event(self):
        """Creates an InfoWindow instance to create new contact."""
        InfoWindow(self.master, self.address_book, self, None)

    def entry_matches(self, event):
        suggest = []
        characters = event.widget.get()
        if characters == '':
            self.frame_search.place_forget()
            return None
        self.frame_search.place(x=1, y=23)
        for name in self.address_book.get_names():
            if characters.lower() in name.lower():
                suggest.append(name)
        for button in self.button_list:
            button.destroy()
        for name in suggest:
            b = Button(master=self.frame_search, text=name, relief=FLAT)
            b.bind("<Button-1>", func=self.show_info_event)
            b.pack()
            self.button_list.append(b)

    def search_event(self, event):
        """"Sends InfoWindow the contact to show if present in address book"""
        contact_name = self.search_entry.get()
        if self.prev_IW_contact is not contact_name:
            self.prev_IW_contact = contact_name
            InfoWindow(self.master, self.address_book, self, contact_name)
