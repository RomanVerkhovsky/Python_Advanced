from tkinter import *
import controller
from settings import *


class GUI(Frame):
    root = Tk()
    root.geometry(size_window)
    root.title(title)

    def __init__(self, master=None) -> None:
        super().__init__(master)
        self.pack()

        self.entry_text = None
        self.entry_id = None
        self.contents = None

        # current_buttons
        self.button_load_notes = None
        self.button_open_note = None
        self.button_add_note = None
        self.button_cancel_add = None
        self.button_create_notes = None

        # container for created widgets
        self.widgets = []

        # current state frame
        self.current_window = self.main_window
        self.current_window()

    def main_window(self) -> None:
        """
        Clearing prev widgets and adding widgets of main window
        :return: None
        """
        self.destroy_into_frame()    # clear frame
        self.current_window = self.main_window
        # create entry text
        self.entry_text = Entry(width=70)
        self.entry_text.pack()

        self.entry_id = None

        # create buttons
        self.button_load_notes = Button(text="Load notes file", command=self.load_notes)
        self.button_load_notes.pack()

        self.button_open_note = Button(text="Open note", command=self.open_note)
        self.button_open_note.pack()

        self.button_add_note = Button(text="Add note", command=self.adding_window)
        self.button_add_note.pack()

        self.widgets = [self.entry_text, self.button_load_notes, self.button_open_note, self.button_add_note]

    def adding_window(self) -> None:
        """
        Clearing prev widgets and adding widgets for adding note
        :return: None
        """
        self.destroy_into_frame()   # clear frame
        self.current_window = self.adding_window

        self.entry_id = Entry()
        self.entry_id.pack()

        self.entry_text = Entry()
        self.entry_text.pack()

        self.button_add_note = Button(text="Add", command=self.add_note)
        self.button_add_note.pack()

        self.button_cancel_add = Button(text="Cancel", command=self.main_window)
        self.button_cancel_add.pack()

        self.widgets = [self.entry_id, self.entry_text, self.button_add_note, self.button_cancel_add]

    def load_notes(self) -> None:
        """
        Downloading notes file from specified path
        :return: None
        """
        result = 'not file'
        if controller.Accession.validate(self.entry_text.get()):
            controller.Accession.load_notes(self.entry_text.get())
            controller.Accession.change_path(self.entry_text.get())
            result = controller.app.get_notes_container().get_dict()

        output = Label(text=result, fg="blue", bg="white", height=3)
        output.pack()

    def add_note(self) -> None:
        """
        Creating and adding new note in notes file
        :return: None
        """
        result = 'id is exist!'
        if not controller.Accession.check_id(self.entry_id.get()):
            controller.Accession.create_note(self.entry_text.get(), self.entry_id.get())
            result = controller.app.get_notes_container().get_dict()

        output = Label(text=result, fg="blue", bg="white", height=3)
        output.pack()
        self.main_window()

    def open_note(self) -> None:
        """
        Opening note from load notes file
        :return: Note
        """
        if len(self.entry_text.get()) != 0:
            result = controller.Accession.open_notes(self.entry_text.get())
            output = Label(text=result, fg="blue", bg="white", height=3)
            output.pack()

    def destroy_into_frame(self) -> None:
        """
        Clearing created widgets in frame
        :return: None
        """
        for item in self.widgets:
            item.destroy()

    def is_notes(self) -> None:
        pass

    def run(self):
        controller.Accession.load_notes(current_path)   # downloading the latest notes file
        self.mainloop()

