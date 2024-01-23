from tkinter import *
import controller
from python_high_difficulty_practices.practice_No_2.Notes.buisness_logic.settings import *


class GUI(Frame):
    root = Tk()
    root.geometry(size_window)
    root.title(title)

    # root.resizable(width=False, height=False)

    def __init__(self, notebook: object, master=None) -> None:

        self.notebook = notebook
        controller.Accession.load_notes(self.notebook, current_path)  # downloading the latest notes file
        super().__init__(master)
        self.pack()

        self.entry_text = None
        self.entry_id = None
        self.contents = None
        self.view_notes = None
        self.scroll = None

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
        self.entry_id = None

        # create buttons
        self.button_load_notes = Button(text="Change notes file", command=self.change_notes_window)
        self.button_load_notes.pack(ipadx='100')

        self.button_open_note = Button(text="Open note", command=self.open_note)
        self.button_open_note.pack(ipadx='30')

        self.button_add_note = Button(text="Add note", command=self.adding_window)
        self.button_add_note.pack(ipadx='30')

        # create entry text
        self.entry_text = Entry(width=70)
        self.entry_text.pack()

        # notes display area
        self.view_notes = Text()
        self.scroll = Scrollbar()
        self.scroll.pack(side=RIGHT, fill=Y)
        self.view_notes.pack()
        self.view()

        self.widgets = [self.entry_text, self.button_load_notes, self.button_open_note, self.button_add_note,
                        self.view_notes, self.scroll]

    def adding_window(self) -> None:
        """
        Clearing prev widgets and adding widgets for adding note
        :return: None
        """
        self.destroy_into_frame()   # clear frame
        self.current_window = self.adding_window

        self.entry_id = Entry()
        self.entry_id.pack()

        self.entry_text = Text()
        self.entry_text.pack()

        self.button_add_note = Button(text="Add", command=self.add_note)
        self.button_add_note.pack()

        self.button_cancel_add = Button(text="Cancel", command=self.main_window)
        self.button_cancel_add.pack()

        self.widgets = [self.entry_id, self.entry_text, self.button_add_note, self.button_cancel_add]

    def change_notes_window(self) -> None:
        self.destroy_into_frame()  # clear frame
        self.current_window = self.main_window

        self.entry_id = None
        self.contents = None
        self.view_notes = None
        self.scroll = None

        self.button_open_note = None
        self.button_add_note = None
        self.button_cancel_add = None
        self.button_create_notes = None

        # input
        self.entry_text = Entry(width=100)
        self.entry_text.pack()

        # current_buttons
        self.button_load_notes = Button(text="load notes file", command=self.load_notes)
        self.button_load_notes.pack(ipadx='25')

        self.button_cancel_add = Button(text="Cancel", command=self.main_window)
        self.button_cancel_add.pack()

        # container for created widgets
        self.widgets = [self.entry_text, self.button_load_notes, self.button_cancel_add]

    def view(self) -> None:
        for item in controller.Accession.get_dict_notes(self.notebook).items():
            text = f'{item[0]}: {item[1]}\n'
            self.view_notes.insert(END, text)

    def load_notes(self) -> None:
        """
        Downloading notes file from specified path
        :return: None
        """
        if controller.Accession.validate(self.entry_text.get()):
            controller.Accession.load_notes(self.notebook, self.entry_text.get())
            controller.Accession.change_path(self.entry_text.get())
            self.main_window()

    def add_note(self) -> None:
        """
        Creating and adding new note in notes file
        :return: None
        """
        if not controller.Accession.check_id(self.notebook, self.entry_id.get()):
            controller.Accession.add_note(self.notebook, self.entry_text.get(1.0, 'end-1c'), self.entry_id.get())
            self.main_window()

    def open_note(self) -> None:
        """
        Opening note from load notes file
        :return: Note
        """
        if len(self.entry_text.get()) != 0:
            result = controller.Accession.open_notes(self.notebook, self.entry_text.get())
            output = Label(text=f'{result[0]}: {result[1]}', fg="blue", bg="white", height=3)
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
        self.mainloop()

