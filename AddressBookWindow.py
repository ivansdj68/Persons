from tkinter import *
from AddressBook import *
from InfoWindow import *

class AddressBookWindow:
    """A window to access an address book's contacts."""

    def __init__(self, master, address_book):
        """Receives a tkinter root and AddressBook instance."""

        # tkinter root is initialized and centered on display
        self.master = master
        self.master.title("Persons")
        self.master.resizable(False, False)
        window_width = 600
        window_height = 300
        display_x = str(self.master.winfo_screenwidth()//2 - window_width//2)
        display_y = str(self.master.winfo_screenheight()//2 - window_height//2)
        self.master.geometry(str(window_width) + 'x' + str(window_height) + '+' + display_x + '+' + display_y)
        self.master.config(bg="black")

        # Section of the window where contact names will be
        self.frame_contacts = Frame(self.master, width=300, height=240, bg="black")

        self.address_book = address_book

        # Tracks currently displayed contact buttons
        self.button_list = []

        # Draws action buttons
        self.add_button = Button(self.master, text="Add", bg=self.master.cget("bg"), fg="white", command=self.add_contact_event)
        self.search_button = Button(self.master, text="Search", bg=self.master.cget("bg"), fg="white")
        self.add_button.place(x=200, y=0)
        self.search_button.place(x=130, y=0)
        self.add_button.bind("<Enter>", self.change_button_color)
        self.add_button.bind("<Leave>", self.change_button_color)
        self.search_button.bind("<Enter>", self.change_button_color)
        self.search_button.bind("<Leave>", self.change_button_color)

        # Draws search entry and binds search_event and entry matches methods
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
        
        # Frame that will contain search matches
        self.frame_search = Frame(self.master)
        self.master.bind("<Double-Button-1>", func=self.des_frame)

        # True if first time drawing names
        self.first = True

        # Tracks if a contact is already on an InfoWindow instance
        self.prev_IW_contact = None

        # Draws names on the root window
        self.draw_names()

    def des_frame(self, event):
        self.frame_search.place_forget()

    def draw_names(self):
        """Makes names list with buttons to access each contact's info"""
        if self.first==False:
           self.remove_contact_buttons()
        self.first = False
        self.frame_contacts.place(x=0, y=60)
        names = self.address_book.get_names()
        for c in names:
            # Draws button with contact name and binds show_info_event method
            button = Button(self.frame_contacts,
                            text=c,
                            relief=FLAT,
                            bg=self.master.cget("bg"),
                            fg="white")
            button.bind("<Button-1>", func=self.show_info_event)
            button.bind("<Enter>", func=self.change_button_color)
            button.bind("<Leave>", func=self.change_button_color)
            button.pack()

    def remove_contact_buttons(self):
        """Destroys current contact buttons"""
        copy_frame = Frame(self.master, width=300, height=240, bg="black")
        self.frame_contacts.destroy()
        self.frame_contacts = copy_frame

    def show_info_event(self, event):
        """Signals the contact to be shown in InfoWindow."""
        self.frame_search.place_forget()
        event.widget.focus_set()
        contact_name = event.widget.cget("text")  # Gets the name of the clicked contact
        if self.prev_IW_contact is not contact_name:
            self.prev_IW_contact = contact_name
            InfoWindow(self.master, self.address_book, self, contact_name)

    def add_contact_event(self):
        """Creates an InfoWindow instance to add a new contact."""
        self.frame_search.place_forget()
        InfoWindow(self.master, self.address_book, self)

    def entry_matches(self, event):
        """Checks if name entered in entry is among existing contacts"""
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
            b = Button(master=self.frame_search, text=name, relief=FLAT, overrelief=GROOVE)
            b.bind("<Button-1>", func=self.show_info_event)
            b.bind("<Enter>", func=self.change_button_color)
            b.bind("<Leave>", func=self.change_button_color)
            b.pack()
            self.button_list.append(b)
    
    def change_button_color(self, event):
        """Changes button color when mouse pointer enters or leaves"""
        button_bg = event.widget.cget("bg")
        if button_bg=="SystemButtonFace":
            event.widget.config(bg="SystemHighlight")
        elif button_bg=="SystemHighlight":
            event.widget.config(bg="SystemButtonFace")
        elif button_bg=="black":
            event.widget.config(bg="SystemButtonShadow")
        elif button_bg=="SystemButtonShadow":
            event.widget.config(bg="black")

    def search_event(self, event):
        """"Sends InfoWindow the contact to show if present in address book"""
        contact_name = self.search_entry.get()
        if contact_name is '':
            return None
        if self.prev_IW_contact is not contact_name:
            self.prev_IW_contact = contact_name
            InfoWindow(self.master, self.address_book, self, contact_name)
