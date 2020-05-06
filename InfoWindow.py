from addressbook import AddressBook
from tkinter import *
from PIL import ImageTk, Image


class InfoWindow:
    def __init__(self, win):
        self.win = win
        self.win.geometry("400x500")
        self.win.grid_columnconfigure(0, weight=1)
        self.win.grid_rowconfigure(0, weight=1)

        self.name = "Mary"
        self.address = "my house"
        self.phone = "787"
        self.email = "name@email.com"

        image = Image.open("blank_profile.jpg")
        # height = 50
        # width = int(height / image.height() * image.width())
        image = image.resize((300, 300), Image.ANTIALIAS)

        self.photo = ImageTk.PhotoImage(image)

        self.frame_photo = Frame(self.win, height=200, width=400)
        self.frame_info = Frame(self.win, height=200, width=400)
        self.frame_button = Frame(self.win, height=100, width=400)

        # self.frame_photo.grid_columnconfigure(0, weight=1)
        # self.frame_photo.grid_rowconfigure(0, weight=1)
        # self.frame_info.grid_columnconfigure(0, weight=1)
        # self.frame_info.grid_rowconfigure(0, weight=1)
        # self.frame_button.grid_columnconfigure(0, weight=1)
        # self.frame_button.grid_rowconfigure(0, weight=1)

        self.frame_photo.grid(row=0,sticky=N)
        self.frame_info.grid(row=1)
        self.frame_button.grid(row=2,sticky=S)

    def show_contact(self):
        self.show_photo()
        Label(self.frame_info, text="Name:", font="Helvetica 15").grid(row=0, column=0, sticky=W,padx=10,pady=10)
        Label(self.frame_info, text="Address:", font="Helvetica 15").grid(row=1, column=0, sticky=W,padx=10,pady=10)
        Label(self.frame_info, text="Phone:", font="Helvetica 15").grid(row=2, column=0, sticky=W,padx=10,pady=10)
        Label(self.frame_info, text="Email:", font="Helvetica 15").grid(row=3, column=0, sticky=W,padx=10,pady=10)

        nameLable = Label(self.frame_info, text=self.name, font="Helvetica")
        nameLable.grid(row=0, column=1, sticky=W)
        addressLable = Label(self.frame_info, text=self.address, font="Helvetica")
        addressLable.grid(row=1, column=1, sticky=W)
        phoneLable = Label(self.frame_info, text=self.phone, font="Helvetica")
        phoneLable.grid(row=2, column=1, sticky=W)
        emailLable = Label(self.frame_info, text=self.email, font="Helvetica")
        emailLable.grid(row=3, column=1, sticky=W)

    def edit_contact(self):
        Label(self.frame_info, text="Name:", font="Helvetica 15").grid(row=0, column=0, sticky=W, padx=10, pady=10)
        Label(self.frame_info, text="Address:", font="Helvetica 15").grid(row=1, column=0, sticky=W, padx=10, pady=10)
        Label(self.frame_info, text="Phone:", font="Helvetica 15").grid(row=2, column=0, sticky=W, padx=10, pady=10)
        Label(self.frame_info, text="Email:", font="Helvetica 15").grid(row=3, column=0, sticky=W, padx=10, pady=10)

        name = Entry(self.frame_info)
        name.insert(END, self.name)
        address = Entry(self.frame_info, textvariable=self.address)
        address.insert(END, self.address)
        phone = Entry(self.frame_info, textvariable=self.phone)
        phone.insert(END, self.phone)
        email = Entry(self.frame_info, textvariable=self.email)
        email.insert(END, self.email)

        name.grid(row=0, column=1)
        address.grid(row=1, column=1)
        phone.grid(row=2, column=1)
        email.grid(row=3, column=1)

        # addressbook method to change a contact
        # contact.setName(name_.get())
        # contact.setAddress(address_.get())
        # contact.setPhone(phone_.get())
        # contact.setEmail(email_.get())

    def new_contact(self):
        Label(self.frame_info, text="Name:", font="Helvetica 15").grid(row=0, column=0, sticky=W, padx=10, pady=10)
        Label(self.frame_info, text="Address:", font="Helvetica 15").grid(row=1, column=0, sticky=W, padx=10, pady=10)
        Label(self.frame_info, text="Phone:", font="Helvetica 15").grid(row=2, column=0, sticky=W, padx=10, pady=10)
        Label(self.frame_info, text="Email:", font="Helvetica 15").grid(row=3, column=0, sticky=W, padx=10, pady=10)

        name = Entry(self.frame_info)
        address = Entry(self.frame_info)
        phone = Entry(self.frame_info)
        email = Entry(self.frame_info)

        name.grid(row=0, column=1)
        address.grid(row=1, column=1)
        phone.grid(row=2, column=1)
        email.grid(row=3, column=1)

    def save_contact(self, name, address, phone, email):
        pass

    def cancel(self):
        pass

    def show_photo(self):
        image = Label(self.frame_photo,image=self.photo,height=200,width=200)
        image.grid(padx=10,pady=10)

    def edit_photo(self):
        pass

    def exit_window(self):
        self.win.destroy()


def main():
    root = Tk()
    IW = InfoWindow(root)
    # IW.show_contact()
    IW.new_contact()
    root.mainloop()


if __name__ == "__main__":
    main()
