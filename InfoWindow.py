from tkinter import filedialog

from addressbook import AddressBook
from tkinter import *
from PIL import ImageTk, Image


class InfoWindow:
    def __init__(self, win):
        self.win = win
        self.win.geometry("400x500")
        self.win.resizable(False, False)
        self.win.grid_columnconfigure(0, weight=1)
        self.win.grid_rowconfigure(0, weight=1)

        self.name = "Mary"
        self.address = "my house"
        self.phone = "787"
        self.email = "name@email.com"

        image = Image.open("blank_profile.jpg")
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

        self.frame_photo.grid(row=0, sticky=N)
        self.frame_info.grid(row=1)
        self.frame_button.grid(row=2, sticky=S)

        self.button = Button(self.frame_button, text="edit", command=self.edit_contact)
        self.button_editPhoto = Button(self.frame_photo, text="edit", command=self.edit_photo)

    def new_contact(self):
        self.create_infoLabel()

        name = Entry(self.frame_info)
        address = Entry(self.frame_info)
        phone = Entry(self.frame_info)
        email = Entry(self.frame_info)

        name.grid(row=0, column=1)
        address.grid(row=1, column=1)
        phone.grid(row=2, column=1)
        email.grid(row=3, column=1)

    def create_infoLabel(self):
        Label(self.frame_info, text="Name:", font="Helvetica 15").grid(row=0, column=0, sticky=W, padx=10, pady=10)
        Label(self.frame_info, text="Address:", font="Helvetica 15").grid(row=1, column=0, sticky=W, padx=10, pady=10)
        Label(self.frame_info, text="Phone:", font="Helvetica 15").grid(row=2, column=0, sticky=W, padx=10, pady=10)
        Label(self.frame_info, text="Email:", font="Helvetica 15").grid(row=3, column=0, sticky=W, padx=10, pady=10)

    def show_contact(self):
        self.show_photo()
        self.create_infoLabel()

        self.nameLabel = Label(self.frame_info, text=self.name, font="Helvetica")
        self.nameLabel.grid(row=0, column=1, sticky=W)
        self.addressLabel = Label(self.frame_info, text=self.address, font="Helvetica")
        self.addressLabel.grid(row=1, column=1, sticky=W)
        self.phoneLabel = Label(self.frame_info, text=self.phone, font="Helvetica")
        self.phoneLabel.grid(row=2, column=1, sticky=W)
        self.emailLabel = Label(self.frame_info, text=self.email, font="Helvetica")
        self.emailLabel.grid(row=3, column=1, sticky=W)

        self.button.grid(sticky=NW)

    def edit_contact(self):
        self.create_infoLabel()

        self.nameLabel.grid_forget()
        self.addressLabel.grid_forget()
        self.phoneLabel.grid_forget()
        self.emailLabel.grid_forget()

        nameEntry = Entry(self.frame_info)
        nameEntry.insert(END, self.name)
        addressEntry = Entry(self.frame_info, textvariable=self.address)
        addressEntry.insert(END, self.address)
        phoneEntry = Entry(self.frame_info, textvariable=self.phone)
        phoneEntry.insert(END, self.phone)
        emailEntry = Entry(self.frame_info, textvariable=self.email)
        emailEntry.insert(END, self.email)

        nameEntry.grid(row=0, column=1)
        addressEntry.grid(row=1, column=1)
        phoneEntry.grid(row=2, column=1)
        emailEntry.grid(row=3, column=1)

        self.button.configure(text="save",command=lambda: self.save_contact(nameEntry.get(), phoneEntry.get(), addressEntry.get(), emailEntry.get()))
        self.button_editPhoto.grid()

    def save_contact(self, name, address, phone, email):
        # self.show_contact()
        pass

    def cancel(self):
        pass

    def show_photo(self):
        self.image = Label(self.frame_photo, image=self.photo, height=200, width=200)
        self.image.grid(padx=10, pady=10)

    def edit_photo(self):
        file_path = filedialog.askopenfilename()

        image = Image.open(file_path)
        image = image.resize((300, 300), Image.ANTIALIAS)

        self.photo = ImageTk.PhotoImage(image)
        self.image.configure(image=self.photo)

    def exit_window(self):
        self.win.destroy()


def main():
    root = Tk()
    IW = InfoWindow(root)
    IW.show_contact()
    # IW.new_contact()
    root.mainloop()


if __name__ == "__main__":
    main()
