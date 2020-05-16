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

        self.frame_contacts = Frame(self.master, width=150, height=240, bg="black")

        self.address_book = address_book

        self.add_button = Button(self.master, text="Add", bg=self.master.cget("bg"), fg="white", command=self.add_contact_event())
        self.sort_button = Button(self.master, text="Sort", bg=self.master.cget("bg"), fg="white", command=self.sort_contact_event())
        self.search_button = Button(self.master, text="Search", bg=self.master.cget("bg"), fg="white")
        self.add_button.place(x=200, y=0)
        self.sort_button.place(x=240, y=0)
        self.search_button.place(x=130, y=0)

        self.search_entry = Entry(self.master,
                                  textvariable="search",
                                  highlightcolor="blue",
                                  highlightbackground="gray",
                                  highlightthickness=1)
        self.search_entry.bind("<Return>", self.search_event)
        self.search_button.bind("<Button-1>", func=self.search_event)
        self.search_entry.place(x=1, y=1)
        self.search_entry.focus_set()

        self.prev_IW_contact = None

        self.sorted = False
        self.change = False
        self.first = True

        self.clicked = None

        self.draw_widgets()

    def draw_names(self):
        # if self.first==False:
        #    self.remove_contact_buttons()
        # self.first = False
        self.frame_contacts.place(x=0, y=60)
        d_y = 60
        names = self.address_book.get_names()
        for c in names:
            button = Button(self.frame_contacts,
                            text=c,
                            relief=FLAT,
                            bg=self.master.cget("bg"),
                            fg="white")
            # Draws button with contact name
            button.bind("<Button-1>", func=self.show_info_event)
            button.pack()

    def assign_option_events(self):
        for b in range(len(self.buttons)):
            current_button = self.buttons[b]
            current_button.config(command=self.option_event_selector(b))

    def draw_widgets(self):
        self.draw_names()
        self.assign_option_events()

    # def remove_contact_buttons(self):
    #     copy_frame = Frame(self.master, width=150, height=240, bg="black")
    #     self.frame_contacts.destroy()
    #     self.frame_contacts = copy_frame

    def show_info_event(self, event):
        self.clicked = event.widget
        contact_name = event.widget.cget("text")  # Gets the name of the clicked contact
        if self.prev_IW_contact is not contact_name:
            self.prev_IW_contact = contact_name
            InfoWindow(self.master, self.address_book, self, contact_name)

    def get_clicked_widget(self):
        return self.clicked

    def add_contact_event(self):
        InfoWindow(self.master, self.address_book, self, None)

    def sort_contacts_event(self):
        if self.sorted == True:
            self.sorted = False
        else:
            self.sorted = True
        sorted_names = self.names
        sorted_names.sort(reverse=self.sorted)
        self.change = True
        self.draw_names(sorted_names)

    def search_event(self, event):
        contact_name = self.search_entry.get()
        if self.prev_IW_contact is not contact_name:
            self.prev_IW_contact = contact_name
            InfoWindow(self.master, self.address_book, self, contact_name)
