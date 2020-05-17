from tkinter import *

root = Tk()
root.geometry("200x200+800+300")

entry = Entry(root)
entry.pack()
entry.focus_set()

address_book = ["Juan Pablo Del Pueblo", "Maria Magdalena del Pilar", "Juan Pedro Del Pueblo", "Maria Gonzalez Cruz"]

button_list = []

def look_for_matches(event):
    suggest = []
    characters = event.widget.get()
    if characters == '':
        return None
    for name in address_book:
        if characters.lower() in name.lower():
            suggest.append(name)
    for button in button_list:
        pass
    for name in suggest:
        b = Button(root, text=name)
        b.pack()
        button_list.append(b)
    print(suggest)

entry.bind("<Key>", look_for_matches)
entry.bind("<Return>", look_for_matches)

root.mainloop()
