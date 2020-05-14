from tkinter import filedialog
from tkinter import *
# from AddressBookWindow import draw_names
from PIL import ImageTk, Image

class InfoWindow:
    def __init__(self, win, address_bookObj, contact_name=None):
        # Draws items to be displayed on screen
        self.frame_photo = Frame(win, height=100, width=300,background="black")
        self.frame_info = Frame(win, height=150, width=300,background="black")
        self.frame_button = Frame(win, height=50, width=300,background="black")
        self.frame_photo.place(x=300, y=0)
        self.frame_info.place(x=300, y=100)
        self.frame_button.place(x=300, y=250)
        
        # Attributes to be utilized
        self.default_Labels = ["Name","Phone","Address","Email"]
        #self.optional_labels = [] #In case if more labels are needed
        self.address_book = address_bookObj
        self.key = contact_name

        # Verifies the status of the incoming contact and what to expect
        if self.key is not None:
            self.contact = self.address_book.search_list(self.key)
            self.show_contact()
        else:
            self.new_contact()


    def default_infoLabel(self):
        """Displays the default labels of a contact"""
        x = 0
        for i in self.default_Labels:
            Label(self.frame_info, text=i+": ").grid(row=x, column=0, sticky=W, padx=10, pady=8)
            x += 1

    def new_contact(self):
        self.default_infoLabel()

        name = Entry(self.frame_info,width=30)
        address = Entry(self.frame_info,width=30)
        phone = Entry(self.frame_info,width=30)
        email = Entry(self.frame_info,width=30)

        name.grid(row=0, column=1)
        address.grid(row=1, column=1)
        phone.grid(row=2, column=1)
        email.grid(row=3, column=1)

        info = [name.get(),phone.get(),address.get(),email.get()]
        contact_information = dict(zip(self.default_Labels,info))

        # button_save_contact = Button(self.frame_info,text="Save", padx=5,
        #                              command=lambda:
        #                              self.save_contact(contact_information))
        self.button1 = Button(self.frame_button, width=10)
        self.button2 = Button(self.frame_button, width=10)
        self.button1.grid(row=0, column=0)
        self.button2.grid(row=0, column=1)

        self.button1.configure(text="save",command=lambda: self.save_contact(contact_information))
        self.button2.configure(text="cancel",command=self.cancel)

    def show_contact(self):
        self.show_photo()
        self.default_infoLabel()

        i = 0
        for k in self.contact:
            value_label = Label(self.frame_info, bg="black",fg="white", text=self.contact.get(k),width=30)
            value_label.grid(row=i,column=1)
            i+=1

        """ self.nameLabel = Label(self.frame_info, text=self.contact.get("Name"),width=30)
        self.nameLabel.grid(row=0, column=1)
        self.phoneLabel = Label(self.frame_info, text=self.contact.get("Phone"),width=30)
        self.phoneLabel.grid(row=1, column=1)
        self.addressLabel = Label(self.frame_info, text=self.contact.get("Address"),width=30)
        self.addressLabel.grid(row=2, column=1)
        self.emailLabel = Label(self.frame_info, text=self.contact.get("Email"),width=30)
        self.emailLabel.grid(row=3, column=1) """

        self.button1 = Button(self.frame_button, width=10)
        self.button2 = Button(self.frame_button, width=10)
        self.button1.grid(row=0, column=0)
        self.button2.grid(row=0, column=1)

        self.button1.configure(text="edit", command=self.edit_contact)
        self.button2.configure(text="delete", command=self.delete_contact)

    def edit_contact(self):
        self.default_infoLabel()

        # self.nameLabel.grid_forget()
        # self.addressLabel.grid_forget()
        # self.phoneLabel.grid_forget()
        # self.emailLabel.grid_forget()

        self.nameEntry = Entry(self.frame_info,width=30)
        self.nameEntry.insert(END, self.contact.get("Name"))
        self.phoneEntry = Entry(self.frame_info,width=30)
        self.phoneEntry.insert(END, self.contact.get("Phone"))
        self.addressEntry = Entry(self.frame_info,width=30)
        self.addressEntry.insert(END, self.contact.get("Address"))
        self.emailEntry = Entry(self.frame_info,width=30)
        self.emailEntry.insert(END, self.contact.get("Email"))

        self.nameEntry.grid(row=0, column=1)
        self.phoneEntry.grid(row=1, column=1)
        self.addressEntry.grid(row=2, column=1)
        self.emailEntry.grid(row=3, column=1)

        self.button_editPhoto = Button(self.frame_photo, text="edit", command=self.edit_photo)
        self.button_editPhoto.grid(row=0, column=1)

        self.button1.configure(text="save",command=lambda: self.save_contact())
        self.button2.configure(text="cancel", command=self.cancel)

    def save_contact(self,name, phone, email, address):
        new_info = [name, phone, email, address]
        if self.address_book.contact_exists(self.key):
            self.address_book.editContact(new_info)
        else:
            self.address_book.add_contact(new_info)
        self.show_contact()

    def delete_contact(self):
        self.address_book.deleteContact(self.key)

    def cancel(self):
        self.button1.grid_forget()
        self.button2.grid_forget()
        self.button_editPhoto.grid_forget()
        self.nameEntry.grid_forget()
        self.phoneEntry.grid_forget()
        self.addressEntry.grid_forget()
        self.emailEntry.grid_forget()

        self.show_contact()

    def show_photo(self):
        image = Image.open("Photos/blank_profile.jpg")
        # FixMe blank profile has to be initialized
        # use if to see how to initialize
        image = image.resize((100, 100), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(image)

        self.image = Label(self.frame_photo, image=self.photo, height=100, width=100)
        self.image.grid(row=0, column=0)

    def edit_photo(self):
        # FixMe need to save the photo
        file_path = filedialog.askopenfilename()

        image = Image.open(file_path)
        image = image.resize((100, 100), Image.ANTIALIAS)

        self.photo = ImageTk.PhotoImage(image)
        self.image.configure(image=self.photo)

    def exit_window(self):
        self.frame_photo.destroy()
        self.frame_info.destroy()
        self.frame_button.destroy()


def main():
    root = Tk()
    IW = InfoWindow(root)
    IW.show_contact()
    # IW.new_contact()
    root.mainloop()


if __name__ == "__main__":
    main()
