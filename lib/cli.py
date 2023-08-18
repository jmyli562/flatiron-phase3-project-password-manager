from sqlalchemy.orm import sessionmaker
from models import User, Category, Entry, Tag, engine
from simple_term_menu import TerminalMenu

# Create the session
Session = sessionmaker(bind=engine)
session = Session()


def main():
    options = ["entry 1", "entry 2", "entry 3"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")


if __name__ == "__main__":
    main()
