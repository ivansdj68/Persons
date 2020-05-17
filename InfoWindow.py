from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

class InfoWindow:
    def __init__(self, win, address_bookObj, abw_obj, contact_name=None):
        # Draws items to be displayed on screen
        self.frame_photo = Frame(win, height=100, width=300, background="black")
        self.frame_info = Frame(win, height=150, width=300, background="black")
        self.frame_button = Frame(win, height=50, width=300, background="black")
        self.frame_photo.place(x=300, y=0)
        self.frame_info.place(x=300, y=100)
        self.frame_button.place(x=300, y=250)

        # draw buttons
        self.button1 = Button(self.frame_button, bg="black", fg="white", width=10)
        self.button2 = Button(self.frame_button, bg="black", fg="white", width=10)
        self.button_editPhoto = Button(self.frame_photo, bg="black", fg="white", text="edit", width=5, command=self.edit_photo)
        # self.button_editPhoto.grid(row=0,column=1)
        self.button1.grid(row=0,column=0,pady=18)
        self.button2.grid(row=0,column=1,pady=18)

        # Entries are made as instance variables to recover text at any moment
        self.name_entry = Entry(self.frame_info, width=30)
        self.address_entry = Entry(self.frame_info, width=30)
        self.phone_entry = Entry(self.frame_info, width=30)
        self.email_entry = Entry(self.frame_info, width=30)
        
        self.photo_path = "Photos/blank_profile.jpg"
        blank_image = Image.open(self.photo_path)
        blank_image = blank_image.resize((100, 100), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(blank_image)
        self.image = Label(self.frame_photo, image=self.photo, height=100, width=100)
        self.image.grid(row=0,column=0)
        
        # Attributes to be utilized
        self.default_Labels = ["Name", "Phone", "Address", "Email"]
        self.address_book = address_bookObj
        self.address_book_window = abw_obj
        self.key = contact_name
        self.contact = None

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
            Label(self.frame_info, bg="black", fg="white", text=i+": ").grid(row=x, column=0, sticky=W, padx=10, pady=8)
            x += 1

    def new_contact(self):
        self.default_infoLabel()

        self.name_entry.grid(row=0, column=1)
        self.phone_entry.grid(row=1, column=1)
        self.address_entry.grid(row=2, column=1)
        self.email_entry.grid(row=3, column=1)

        self.button1.configure(text="save", command=self.save_contact)
        self.button2.configure(text="cancel", command=self.exit_window)
        self.button_editPhoto.grid(row=0, column=1)

    def show_contact(self):
        self.show_photo()
        self.default_infoLabel()

        i = 0
        for k in self.default_Labels:
            value_label = Label(self.frame_info, bg="black",fg="white", text=self.contact.get(k), width=30)
            value_label.grid(row=i, column=1)
            i+=1

        self.button1.configure(text="edit", command=self.edit_contact)
        self.button2.configure(text="delete", command=self.delete_contact)

    def edit_contact(self):
        self.frame_info.grid_forget()

        self.default_infoLabel()

        self.name_entry = Entry(self.frame_info, width=30)
        self.name_entry.insert(END, self.contact.get("Name"))
        self.phone_entry = Entry(self.frame_info, width=30)
        self.phone_entry.insert(END, self.contact.get("Phone"))
        self.address_entry = Entry(self.frame_info, width=30)
        self.address_entry.insert(END, self.contact.get("Address"))
        self.email_entry = Entry(self.frame_info, width=30)
        self.email_entry.insert(END, self.contact.get("Email"))

        self.name_entry.grid(row=0, column=1)
        self.phone_entry.grid(row=1, column=1)
        self.address_entry.grid(row=2, column=1)
        self.email_entry.grid(row=3, column=1)

        self.button1.configure(text="save", command=self.save_contact)
        self.button2.configure(text="cancel", command=self.show_contact)
        self.button_editPhoto.grid(row=0, column=1)

    def save_contact(self):
        new_info = [self.name_entry.get(), self.phone_entry.get(), self.address_entry.get(),self.email_entry.get()]
        contact_information = dict(zip(self.default_Labels, new_info))

        #creates photo field
        contact_photo = {"Photo": self.photo_path}
        contact_information.update(contact_photo)

        if self.address_book.contact_exists(self.key):
            self.address_book.edit_contact(self.key, contact_information)
        else:
            self.address_book.add_contact(contact_information)
            self.address_book_window.draw_names()
        
        self.key = contact_information["Name"]
        self.contact = contact_information
        self.address_book_window.draw_names()
        self.show_contact()

    def delete_contact(self):
        self.address_book.delete_contact(self.key)
        self.address_book_window.draw_names()
        self.exit_window()

    def show_photo(self):
        try:
            image = Image.open(self.contact.get("Photo"))
        except AttributeError:
            image = Image.open("Photos/blank_profile.jpg")
        image = image.resize((100, 100), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(image)
        self.image.configure(image=self.photo)

    def edit_photo(self):
        self.photo_path = filedialog.askopenfilename()

        image = Image.open(self.photo_path)
        image = image.resize((100, 100), Image.ANTIALIAS)

        self.photo = ImageTk.PhotoImage(image)
        self.image.configure(image=self.photo)

    def exit_window(self):
        self.frame_photo.destroy()
        self.frame_info.destroy()
        self.frame_button.destroy()


# def main():
#     root = Tk()
#     IW = InfoWindow(root)
#     IW.show_contact()
#     # IW.new_contact()
#     root.mainloop()


# if __name__ == "__main__":
#     main()
