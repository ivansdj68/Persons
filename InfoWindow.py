from tkinter import *
from AddressBook import *

class InfoWindow:
    def __init__(self, win, address_bookObj, abw_obj, contact_name=None):
        self.canvas = Canvas(master=win, width=295, height=295, bg="black", highlightcolor="yellow")
        self.canvas.focus_set()
        self.canvas.place(x=300, y=0)

        self.edit_button = Button(self.canvas, text="Edit", bg="black", fg="white",
                                  command=lambda: self.edit_contact())

        self.save_contact_button = Button(self.canvas, text="Save", bg="black", fg="white")

        self.delete_contact_button = Button(self.canvas, text="Delete", bg="black", fg="white",
                                            command=lambda: self.delete_contact())

        self.cancel_button = Button(self.canvas, text="Cancel", bg="black", fg="white",
                                    command=lambda: self.cancel())

        self.stay_in_IW = True

        self.address_book = address_bookObj

        self.address_book_window = abw_obj

        if contact_name != "new":
            self.contact = self.address_book.searchList(contact_name)
            self.show_contact()
        else:
            self.new_contact()

    def create_info_labels(self):
        Label(self.canvas, text="Name:", bg="black", fg="white").place(x=30, y=60)
        Label(self.canvas, text="Phone:", bg="black", fg="white").place(x=30, y=90)
        Label(self.canvas, text="Email:", bg="black", fg="white").place(x=30, y=120)
        Label(self.canvas, text="Address:", bg="black", fg="white").place(x=30, y=150)

    def create_contact_labels(self):
        contact_name_label = Label(self.canvas, text=self.contact.get("Name"), width=30, bg="black", fg="white")
        contact_phone_label = Label(self.canvas, text=self.contact.get("Phone"), width=30, bg="black", fg="white")
        contact_email_label = Label(self.canvas, text=self.contact.get("Email"), width=30, bg="black", fg="white")
        contact_address_label = Label(self.canvas, text=self.contact.get("Address"), width=30, bg="black", fg="white")
        contact_name_label.place(x=80, y=60)
        contact_phone_label.place(x=80, y=90)
        contact_email_label.place(x=80, y=120)
        contact_address_label.place(x=80, y=150)

    def show_contact(self):
        self.create_info_labels()
        self.create_contact_labels()
        self.save_contact_button.place_forget()
        self.edit_button.place(x=160, y=200)
        self.delete_contact_button.place(x=200, y=200)
        self.cancel_button.place(x=250, y=200)
        self.stay_in_IW = False

    def edit_contact(self):
        self.edit_button.place_forget()
        self.delete_contact_button.place_forget()
        self.stay_in_IW = True

        name_ = Entry(self.canvas, width=35)
        phone_ = Entry(self.canvas, width=35)
        email_ = Entry(self.canvas, width=35)
        address_ = Entry(self.canvas, width=35)
        name_.insert(END, self.contact.get("Name"))
        phone_.insert(END, self.contact.get("Phone"))
        email_.insert(END, self.contact.get("Email"))
        address_.insert(END, self.contact.get("Address"))
        name_.place(x=80, y=60)
        phone_.place(x=80, y=90)
        email_.place(x=80, y=120)
        address_.place(x=80, y=150)

        self.save_contact_button.config(command=lambda:
                                        self.save_contact(name_.get(), phone_.get(), email_.get(), address_.get()))
        self.save_contact_button.place(x=200, y=200)

    def new_contact(self):
        self.edit_button.place_forget()
        self.create_info_labels()

        name_ = Entry(self.canvas, width=35)
        phone_ = Entry(self.canvas, width=35)
        email_ = Entry(self.canvas, width=35)
        address_ = Entry(self.canvas, width=35)

        name_.place(x=80, y=60)
        phone_.place(x=80, y=90)
        email_.place(x=80, y=120)
        address_.place(x=80, y=150)

        self.save_contact_button.config(command=lambda:
                                        self.save_contact(name_.get(), phone_.get(), email_.get(), address_.get()))
        self.save_contact_button.place(x=200, y=200)

        self.cancel_button.place(x=250, y=200)

        self.stay_in_IW = False

    def save_contact(self, name, phone, email, address):
        new_info = [name, phone, email, address]
        if self.stay_in_IW is True and self.address_book.isNameInAddressBook(self.contact["Name"]):
            self.address_book.editContact(new_info)
        else:
            self.address_book.add_contact(new_info)
            self.contact = self.address_book.searchList(new_info[0])
            self.show_contact()
            self.address_book_window.draw_widgets()

    def delete_contact(self):
        self.address_book.deleteContact(self.contact["Name"])
        self.address_book_window.draw_widgets()
        self.canvas.destroy()

    def cancel(self):
        if self.stay_in_IW:
            self.show_contact()
        else:
            self.canvas.destroy()
