from contacts import Contacts
from tkinter import *
from PIL import ImageTk, Image


class InfoWindow:
    def __init__(self, win, contact):
        self.win = win

        self.contact = contact
        self.name = self.contact.getName()
        self.address = self.contact.getAddress()
        self.phone = self.contact.getPhone()
        self.email = self.contact.getEmail()
        image = Image.open(self.contact.getPhoto())
        self.photo = ImageTk.PhotoImage(image)
        # self.frame = Frame(self.win,width=200, height=200)

        self.button_new_contact = Button(text="Add Contact", command=self.new_contact)
        self.button_new_contact.grid(row=3, column=3)
        self.button_show_contact = Button(text="Show contact", command=self.show_contact)
        self.button_show_contact.grid(row=3, column=4)
        self.button_edit = Button(text="edit", command=lambda: self.edit_contact(self.contact))
        self.button_cancel = Button(text="Cancel", padx=5, command=self.cancel)

    def show_contact(self):
        self.button_show_contact.grid_forget()
        self.button_new_contact.grid_forget()

        # canvas = Canvas(self.win, width=100, height=100)
        # canvas.grid(row=0, column=0)
        # canvas.create_image(10, 10, image=self.photo)
        self.show_photo()
        Label(self.win, text="Name:").grid(row=1,column=0)
        Label(self.win, text="Address:").grid(row=2,column=0)
        Label(self.win, text="Phone:").grid(row=3,column=0)
        Label(self.win, text="Email:").grid(row=4,column=0)

        namelable = Label(self.win, text=self.name)
        namelable.grid(row=1, column=2)
        addresslable = Label(self.win, text=self.address)
        addresslable.grid(row=2, column=2)
        phonelable = Label(self.win, text=self.phone)
        phonelable.grid(row=3, column=2)
        emaillable = Label(self.win, text=self.email)
        emaillable.grid(row=4, column=2)

        self.button_edit.grid(row=4, column=4)

    def edit_contact(self, contact):
        self.button_edit.grid_forget()
        Label(self.win, text="Name:").grid(row=0)
        Label(self.win, text="Address:").grid(row=1)
        Label(self.win, text="Phone:").grid(row=2)
        Label(self.win, text="Email:").grid(row=3)

        name_ = Entry(self.win)
        name_.insert(END, self.name)
        address_ = Entry(self.win, textvariable=contact.getAddress())
        address_.insert(END, self.address)
        phone_ = Entry(self.win, textvariable=contact.getPhone())
        phone_.insert(END, self.phone)
        email_ = Entry(self.win, textvariable=contact.getEmail())
        email_.insert(END, self.email)

        name_.grid(row=0, column=1)
        address_.grid(row=1, column=1)
        phone_.grid(row=2, column=1)
        email_.grid(row=3, column=1)

        # addressbook method to change a contact
        contact.setName(name_.get())
        contact.setAddress(address_.get())
        contact.setPhone(phone_.get())
        contact.setEmail(email_.get())

        button_new_contact = Button(text="Save", padx=5,
                                    command=lambda: self.save_contact(name_.get(), address_.get(), phone_.get(),
                                                                      email_.get()))
        button_new_contact.grid(row=3, column=4)
        button_cancel = Button(text="Cancel", padx=5, command=self.cancel)
        button_cancel.grid(row=3, column=5)

        # contact is saving twice, fix

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

        self.button_save_contact = Button(text="Save", padx=5,
                                          command=lambda: self.save_contact(name_.get(), address_.get(), phone_.get(),
                                                                            email_.get()))
        self.button_save_contact.grid(row=3, column=3)
        self.button_cancel.grid(row=3, column=4)

    def save_contact(self, name, address, phone, email):
        file = open("contacts.txt", "a")
        file.write(str(name))
        file.write(" ")
        file.write(str(address))
        file.write(" ")
        file.write(str(phone))
        file.write(" ")
        file.write(str(email))
        file.write('\n')
        file.close()
        # add to contact list

    def cancel(self):
        pass

    def show_photo(self):
        #resize height and width
        canvas = Canvas(self.win, width=100, height=100)
        canvas.grid(row=0, column=0)
        canvas.create_image(10, 10, image=self.photo)


    def edit_photo(self):
        pass

    def exit_window(self):
        self.win.destroy()


def main():
    root = Tk()
    contact = Contacts("name", "phone", "email", "address")
    InfoWindow(root, contact)
    root.mainloop()


if __name__ == "__main__":
    main()
