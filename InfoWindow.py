from tkinter import *

class InfoWindow:

    def __init__(self, master, contactObj):
        self.contact = contactObj
        self.master = master
        self.frame = Frame(self.master, width=200, height=200)
        self.buttons = [Button(self.master, text="Save")]
        self.entry = [Entry(self.master, text="Name"),
                      Entry(self.master, text="Phone"),
                      Entry(self.master, text="Email"),
                      Entry(self.master, text="Address")]
        self.profilePic = PhotoImage()
        self.drawContactInfo()

    def drawContactInfo(self):
        nameLabel = Label(self.master, text=self.contact.getName())
        phoneLabel = Label(self.master, text=self.contact.getPhone())
        emailLabel = Label(self.master, text=self.contact.getEmail())
        addressLabel = Label(self.master, text=self.contact.getAddress())
        nameLabel.grid()
        phoneLabel.grid()
        emailLabel.grid()
        addressLabel.grid()
