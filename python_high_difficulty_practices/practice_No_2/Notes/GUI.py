from tkinter import *
import controller


class GUI(Frame):
    root = Tk()
    root.geometry('800x500')

    def __init__(self, master=None):

        super().__init__(master)
        self.pack()

        self.entry_text = None
        self.entry_id = None

        self.contents = None

        self.button_load_notes = None
        self.button_open_note = None

        self.button_create_note = None

        self.widgets = []

        self.current_window = self.main_window
        self.current_window()

    def main_window(self) -> None:
        self.destroy_into_frame()

        self.current_window = self.main_window

        self.entry_text = Entry()
        self.entry_text.pack()

        self.contents = StringVar()
        self.contents.set('data/1.txt')

        self.entry_text['text'] = self.contents

        self.entry_id = None

        self.button_load_notes = Button(text="load", command=self.load_notes)
        self.button_load_notes.pack()

        self.button_open_note = Button(text="read", command=self.open_note)
        self.button_open_note.pack()

        self.button_create_note = Button(text="create", command=self.creation_window)
        self.button_create_note.pack()

        self.widgets.append(self.entry_text)

    def creation_window(self) -> None:
        self.destroy_into_frame()

        self.update()

        self.current_window = self.creation_window

        self.entry_id = Entry()
        self.entry_id.pack()

        self.entry_text = Entry()
        self.entry_text.pack()

        self.button_create_note = Button(text="create", command=self.create_note)
        self.button_create_note.pack()

    def destroy_into_frame(self) -> None:
        for item in self.widgets:
            item.destroy()

        print(self.widgets)

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
        controller.Accession.create_note(self.entry_text.get(), self.entry_id.get())

        result = controller.app.get_notes_container().get_dict()
        output = Label(text=result, fg="blue", bg="white", height=3)
        output.pack()
        self.main_window()

    def run(self):
        self.mainloop()

