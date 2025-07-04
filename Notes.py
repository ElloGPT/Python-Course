from dataclasses import dataclass, field
from uuid import uuid4, UUID

@dataclass
class Note:
    id: UUID = field(init=False)
    title: str
    body: str

    def __post_init__(self) -> None:
        self.id = uuid4()

class NoteApp:
    def __init__(self, author: str, notes: list[Note] | None = None) -> None:
        self.author = author
        

        if notes is None:
            self._notes = []
        else:
            self._notes = notes

        self.display_instruction()

    @staticmethod
    def display_instruction() -> None:
            print("Welcome to Notes!")
            print("Options:")
            print("1 - Add new Note")
            print("2 - Edit Note")
            print("3 - Delete Note")
            print("4 - Display all Notes")

    def _add_note(self) -> None:
            title: str = input("Title:")
            body: str = input("Body:")

            note: Note = Note(title, body)
            self._notes.append(note)
            print("Note was added!")

    def _edit_note(self) -> None:
            print("Which Note do you want to edit?")
            self._show_notes()

            try:
                note_index: int = int(input("Index: ")) -1
                current: Note = self._notes[note_index]

                new_title: str = input("New title: ")
                new_body: str = input("New body: ")

                current.title = new_title
                current.body = new_body
                print("Note was updated!")
            except IndexError:
                print("Please select a valid note index...")
                self._edit_note()
            except ValueError:
                print("Index can not be empty!")
                print("Aborting operation")

    def _delete_note(self) -> None:
        print("Which Note do you want to delete?")
        self._show_notes()

        try:
            note_index: int = int(input("Index: ")) -1
            del self._notes[note_index]
            print("Note was deleted!")
        except IndexError:
            print("Please select a valid note index...")
            self._delete_note()
        except ValueError:
            print("Index can not be empty!")
            print("Aborting operation")


    def _show_notes(self) -> None:
        if not self._notes:
            print("No notes..")
            return
            
        for i, note in enumerate(self._notes, start=1):
                print(f"[{i}] {note.title}: {note.body}")

    def _select_option(self, user_input: str) -> None:
        if user_input not in ["1", "2", "3", "4"]:
                print("Please pick a valid option!")
                return

        if user_input == "1":
                self._add_note()
        elif user_input == "2":
                self._edit_note()
        elif user_input == "3":
                self._delete_note()
        elif user_input == "4":
                self._show_notes()

    def run_app(self) -> None:
        while True:
            user_input: str = input("You:")
            self._select_option(user_input)
        

def main() -> None:
    sample_notes: list[Note] = [Note(title="Title1", body="Hello there :D"),
                                      Note(title="Title2", body="I am ElloGPT"),
                                      Note(title="Title3", body="Dont forgett to code today!")]

    noteApp: NoteApp = NoteApp(author="ElloGPT", notes=sample_notes) 
    noteApp.run_app()


if __name__ == "__main__":
    main()

#to do list: no empty notes, exit option, display all command again (fifth option), 