from notebook import Notebook, Note
import sys


class Menu:
    """
    Display a menu and respond to choices when run
    """

    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit
        }

    def display_menu(self):
        print("""
        Notebook Menu
        
        1. Show all Notes
        2. Search Notes
        3. Add Note
        4. Modify Note
        5. Quit
        """)

    def run(self):
        """
        Display the menu and respond to choices
        :return: N/A
        """
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{} is not a valid choice.".format(choice))

    def show_notes(self, notes=None):
        """
        prints passed note objects to terminal, or if no note
        objects passed, will print every note in notebook
        :param notes: note object to print to terminal
        :return: note object's id, tag, and memo
        """
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print("{}: {}\n{}".format(note.id, note.tags, note.memo))

    def search_notes(self):
        """
        Search through all the notes and return note objects
        that match whatever the user inputs
        :return: note object array that matches input
        """
        filter_string = input("Search for: ")
        notes = self.notebook.search(filter_string)
        self.show_notes(notes)

    def add_note(self):
        """
        Adds a new note to the notebook with no tag
        :return: notebook updated with note
        """
        memo = input("Enter a memo: ")
        self.notebook.new_note(memo)
        print("Your note has been added.")

    def modify_note(self):
        """
        modifies a current note in the notebook's memo, id, and
        tags with user input
        :return: notebook updated with a current notes memo, id,
        and tag updated with user input
        """
        id = input("Enter a note id: ")
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_memo(id, tags)

    def quit(self):
        """
        Prints goodbye and quits the terminal menu with exit
        code 0
        :return: N/A
        """
        print("Thank you for using your notebook today")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()
