from tkinter import *
from AddressBook import *


class InfoWindow:
    def __init__(self, win, address_bookObj, contact_name=None):
        self.canvas = Canvas(master=win, width=300, height=300)
        self.canvas.place(x=300, y=0)

        self.address_book = address_bookObj

        if contact_name is not None:
            self.contact = self.address_book.searchList(contact_name)
        else:
            self.new_contact()

        self.name_label = Label(self.canvas, text="Name:")
        self.phone_label = Label(self.canvas, text="Phone:")
        self.email_label = Label(self.canvas, text="Email:")
        self.address_label = Label(self.canvas, text="Address:")
        self.name_label.place(x=30, y=60)
        self.phone_label.place(x=30, y=90)
        self.email_label.place(x=30, y=120)
        self.address_label.place(x=30, y=150)

        self.contact_name_label = Label(self.canvas, text=self.contact.get("Name"))
        self.contact_phone_label = Label(self.canvas, text=self.contact.get("Phone"))
        self.contact_email_label = Label(self.canvas, text=self.contact.get("Email"))
        self.contact_address_label = Label(self.canvas, text=self.contact.get("Address"))
        self.contact_name_label.place(x=80, y=60)
        self.contact_phone_label.place(x=80, y=90)
        self.contact_email_label.place(x=80, y=120)
        self.contact_address_label.place(x=80, y=150)

        #  self.button_cancel = Button(text="Cancel", padx=5, command=self.exit_window)

    def show_contact(self):
        Label(self.canvas, text="Name:").place(x=0, y=30)
        Label(self.canvas, text="Phone:").pack()
        Label(self.canvas, text="Email:").pack()
        Label(self.canvas, text="Address:").pack()

        name_label = Label(self.canvas, text=self.contact.get("Name"))
        name_label.pack()
        phone_label = Label(self.canvas, text=self.contact.get("Phone"))
        phone_label.pack()
        email_label = Label(self.canvas, text=self.contact.get("Email"))
        email_label.pack()
        address_label = Label(self.canvas, text=self.contact.get("Address"))
        address_label.pack()
        button_edit = Button(text="Edit", command=lambda: self.edit_contact)
        button_edit.pack()

    def edit_contact(self):
        Label(self.canvas, text="Name:").pack()
        Label(self.canvas, text="Address:").pack()
        Label(self.canvas, text="Phone:").pack()
        Label(self.canvas, text="Email:").pack()

        name_ = Entry(self.canvas, textvariable=self.contact.get("Name"))
        phone_ = Entry(self.canvas, textvariable=self.contact.get("Phone"))
        email_ = Entry(self.canvas, textvariable=self.contact.get("Email"))
        address_ = Entry(self.canvas, textvariable=self.contact.get("Name"))

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
        Label(self.canvas, text="Name:").grid(row=0)
        Label(self.canvas, text="Address:").grid(row=1)
        Label(self.canvas, text="Phone:").grid(row=2)
        Label(self.canvas, text="Email:").grid(row=3)

        name_ = Entry(self.canvas)
        address_ = Entry(self.canvas)
        phone_ = Entry(self.canvas)
        email_ = Entry(self.canvas)

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

    def clearWidgets(self):
        self.name_label.pack_forget()
        self.phone_label.pack_forget()
        self.email_label.pack_forget()
        self.address_label.pack_forget()
        self.contact_name_label.pack_forget()
        self.contact_name_label.pack_forget()
        self.contact_phone_label.pack_forget()
        self.contact_email_label.pack_forget()
        self.contact_address_label.pack_forget()

    # def show_photo(self):
    #     #resize height and width
    #     canvas = Canvas(self.canvas, width=100, height=100)
    #     canvas.grid(row=0, column=0)
    #     canvas.create_image(10, 10, image=self.photo)
    #
    #
    # def edit_photo(self):
    #     pass

    def exit_window(self):
        self.canvas.destroy()

# def main():
#     root = Tk()
#     #contact = Contacts("name", "phone", "email", "address")
#     InfoWindow(root)
#     root.mainloop()
#
# main()
