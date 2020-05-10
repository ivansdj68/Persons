from tkinter import *
from AddressBook import *


class InfoWindow:
    def __init__(self, win, address_bookObj, contact_name=None):
        self.win = win
        self.address_book = address_bookObj
        if contact_name is not None:
            self.contact = self.address_book.searchList(contact_name)
            self.show_contact()
        else:
            self.new_contact()
        self.button_cancel = Button(text="Cancel", padx=5, command=self.exit_window)

    def show_contact(self):
        Label(self.win, text="Name:").place(x=0, y=30)
        Label(self.win, text="Phone:").pack()
        Label(self.win, text="Email:").pack()
        Label(self.win, text="Address:").pack()

        name_label = Label(self.win, text=self.contact.get("Name"))
        name_label.pack()
        phone_label = Label(self.win, text=self.contact.get("Phone"))
        phone_label.pack()
        email_label = Label(self.win, text=self.contact.get("Email"))
        email_label.pack()
        address_label = Label(self.win, text=self.contact.get("Address"))
        address_label.pack()
        button_edit = Button(text="Edit", command=lambda: self.edit_contact)
        button_edit.pack()

    def edit_contact(self):
        Label(self.win, text="Name:").pack()
        Label(self.win, text="Address:").pack()
        Label(self.win, text="Phone:").pack()
        Label(self.win, text="Email:").pack()

        name_ = Entry(self.win, textvariable=self.contact.get("Name"))
        phone_ = Entry(self.win, textvariable=self.contact.get("Phone"))
        email_ = Entry(self.win, textvariable=self.contact.get("Email"))
        address_ = Entry(self.win, textvariable=self.contact.get("Name"))

        name_.pack()
        name_.focus()
        phone_.pack()
        email_.pack()
        address_.pack()

        button_save_contact = Button(text="Save", padx=5,
                                     command=lambda:
                                     self.save_contact(name_.get(), phone_.get(), email_.get(), address_.get()))
        button_save_contact.pack()

    def new_contact(self):
        self.button_new_contact.grid_forget()
        self.button_show_contact.grid_forget()
        Label(self.win, text="Name:").grid(row=0)
        Label(self.win, text="Address:").grid(row=1)
        Label(self.win, text="Phone:").grid(row=2)
        Label(self.win, text="Email:").grid(row=3)

        name_ = Entry(self.win)
        address_ = Entry(self.win)
        phone_ = Entry(self.win)
        email_ = Entry(self.win)

        name_.grid(row=0, column=1)
        address_.grid(row=1, column=1)
        phone_.grid(row=2, column=1)
        email_.grid(row=3, column=1)

        button_save_contact = Button(text="Save", padx=5,
                                     command=lambda:
                                     self.save_contact(name_.get(), phone_.get(), email_.get(), address_.get()))
        button_save_contact.pack()
        self.button_cancel.pack()

    def save_contact(self, name, phone, email, address):
        new_info = [name, phone, email, address]
        if self.address_book.isNameInAddressBook(self.contact["Name"]):
            self.address_book.editContact(new_info)
        else:
            self.address_book.add_contact(new_info)

    def delete_contact(self):
        self.address_book.deleteContact(self.contact["Name"])

    def cancel(self):
        pass

    # def show_photo(self):
    #     #resize height and width
    #     canvas = Canvas(self.win, width=100, height=100)
    #     canvas.grid(row=0, column=0)
    #     canvas.create_image(10, 10, image=self.photo)
    #
    #
    # def edit_photo(self):
    #     pass

    def exit_window(self):
        self.win.destroy()

# def main():
#     root = Tk()
#     #contact = Contacts("name", "phone", "email", "address")
#     InfoWindow(root)
#     root.mainloop()
#
# main()
