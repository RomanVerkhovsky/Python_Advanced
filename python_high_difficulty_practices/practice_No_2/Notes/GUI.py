from tkinter import *
import controller


class GUI(Frame):
    root = Tk()
    root.geometry('800x500')

    def __init__(self, master=None):

        super().__init__(master)
        self.pack()

        self.entry_text = Entry()
        self.entry_text.pack()

        self.contents = StringVar()
        self.contents.set('1.txt')

        self.entry_text['text'] = self.contents

        self.button_load_notes = Button(master, text="load", command=self.load_notes)
        self.button_load_notes.pack()

        self.button_open_note = Button(master, text="read", command=self.open_note)
        self.button_open_note.pack()

        self.button_create_note = Button(master, text="create", command=self.create_note)
        self.button_create_note.pack()

    def creating_window(self):
        self.entry_text = Entry()
        self.entry_text.pack()

    def load_notes(self):
        if controller.Accession.validate(self.entry_text.get()):
            controller.Accession.load_notes(self.entry_text.get())
            result = controller.app.get_notes_container().get_dict()
            output = Label(text=result, fg="blue", bg="white", height=3)
            output.pack()
        else:
            result = 'not file'
            output = Label(text=result, fg="blue", bg="white", height=3)
            output.pack()

    def open_note(self):
        result = controller.Accession.open_notes(self.entry_text.get())
        print(result)
        output = Label(text=result, fg="blue", bg="white", height=3)
        output.pack()

    def create_note(self):
        self.creating_window()
        result = controller.app.get_notes_container().get_dict()
        output = Label(text=result, fg="blue", bg="white", height=3)
        output.pack()

    def run(self):
        self.mainloop()

