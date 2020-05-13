from tkinter import *
from AddressBook import *
from InfoWindow import *

class AddressBookWindow:

    def __init__(self, master, address_book):
        #Creates Window
        self.master = master
        window_width = 300*2
        window_height = 150*2
        display_x = str(self.master.winfo_screenwidth()//2 - window_width//2)
        display_y = str(self.master.winfo_screenheight()//2 - window_height//2)
        self.master.geometry(str(window_width) + 'x' + str(window_height) + '+' + display_x + '+' + display_y)

        # Draws AddressBookWindow Frame
        self.ABWFrame = Frame(master=self.master, height=0, width=window_width//2)
        self.ABWFrame.place(x=0, y=0)   
        # Creates buttons
        self.buttons = [Button(self.master, text="Add"), Button(self.master, text="Sort"),
                        Button(self.master, text="Search")]
        self.buttons[0].place(x=200, y=0)
        self.buttons[1].place(x=240, y=0)
        self.buttons[2].place(x=140, y=0)
        # Draws search box
        self.search_entry = Entry(self.master, text="Search Contact")
        self.search_entry.bind("<Return>", self.search_event)
        self.search_entry.place(x=10, y=0)
        # Attributes 
        self.adBook = address_book
        self.names = self.adBook.get_names()
        self.sorted = False
        self.prev_IW_contact = None
        self.change = False
        self.name_button = []

        self.draw_widgets()

    def draw_names(self,newnames):
        button = self.name_button
        pos,i = 60,0

        if newnames == self.names:
            local_names = self.names
        else:
            local_names = newnames
            

        if self.change == False:
            for c in local_names:
                button.append(Button(self.master, text=c,bd=0,activebackground='gray'))  # Draws button with contact name
            for b in button:
                b.bind("<Button-1>", func=self.show_info_event)
                b.place(x=0, y=pos)
                pos += 26
        else:
            for b in button:
                b.config(text=local_names[i])
                i+=1
            self.change = False

    def assign_option_events(self):
        for b in range(len(self.buttons)):
            current_button = self.buttons[b]
            current_button.bind("<Button-1>", func=self.option_event_selector(b))

    def draw_widgets(self):
        self.draw_names(self.names)
        self.assign_option_events()

    def show_info_event(self, event):
        contact_name = event.widget.cget("text")  # Gets the name of the clicked contact
        if self.prev_IW_contact is not contact_name:
            InfoWindow(self.master, self.adBook, contact_name)
            self.prev_IW_contact = contact_name

    def option_event_selector(self, num):
        if num == 0:
            return self.add_contact_event
        elif num == 1:
            return self.sort_contacts_event
        elif num == 2:
            return self.search_event

    def add_contact_event(self, event):
        InfoWindow(self.ABWFrame, self.adBook, None)

    def sort_contacts_event(self, event):
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
        found =  [idx for idx in self.names if idx.lower().startswith(contact_name.lower())] # List with contacts that match\
        self.change = True
        self.draw_names(found)

root = Tk()
#root.withdraw Withdraw this widget from the screen such that it is unmapped and forgotten by the window manager. Re-draw it with wm_deiconify.

ab = AddressBook()
AddressBookWindow(root, ab)
root.mainloop()
