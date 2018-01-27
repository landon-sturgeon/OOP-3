import datetime

# Store the next available id for all new notes
last_id = 0


class Note(object):
    """
    Represent a note in the notebook. Match against a
    string in seraches and store tags for each note.
    """

    def __init__(self, memo, tags=""):
        """
        space-separated tags. Automatically set the note's
        creation date and a unique id
        :param memo: the actual note being generated
        :param tags: tags to be used for classification
        :return: N/A
        """
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        """
        Determine if this note matches the filter text.
        Return True if it matches, False otherwise.

        Search is case sensitive and matches both text and tags
        :param filter: string to match against memo or tag
        :return: bool for value found or not
        """
        return filter in self.memo or filter in self.tags


class Notebook(object):
    """
    Represent a collection of notes that can be tagged,
    modified and searched
    """

    def __init__(self):
        """
        Initialize a notebook with an empty list.
        """
        self.notes = []

    def new_note(self, memo, tags=""):
        """
        Create a new note and add it to the list
        :param memo: text of new note to be created
        :param tags: text attached to note for easy classification
        :return: appends new note to self.notes
        """
        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id):
        """
        Locate the note with the given id
        :param note_id: unique note id to identify specific note
        :return: note object with matched note_id
        """
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None

    def modify_memo(self, note_id, memo):
        """
        Find the note with the given id and change its
        memo to the given value
        :param note_id: unique note id to identify specific note
        :param memo: new text to change the note to
        :return: N/A
        """
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False

    def modify_tags(self, note_id, tags):
        """
        Find the note with the given id and change its tags
        to the given value
        :param note_id: unique note id to identify specific note
        :param tags: new text to change the note's tag to
        :return: N/A
        """
        note = self._find_note(note_id)
        if note:
            note.tags = tags
            return True
        return False

    def search(self, filter_string):
        """
        Find all notes that match the given filter string
        :param filter_string: string to find in note or tag
        :return: returns note class objects
        """
        return [note for note in self.notes if note.match(filter_string)]
