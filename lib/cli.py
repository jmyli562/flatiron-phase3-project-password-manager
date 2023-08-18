from sqlalchemy.orm import sessionmaker
from models import User, Category, Entry, Tag, engine
from simple_term_menu import TerminalMenu

# Create the session
Session = sessionmaker(bind=engine)
session = Session()


def login():
    pass


def add_user():
    pass


def main():
    options = ["Login", "Create Account", "Exit"]
    terminal_menu = TerminalMenu(options)

    while True:
        user_selection = terminal_menu.show()
        if user_selection == 0:
            login()
        elif user_selection == 1:
            add_user()
        elif user_selection == 2:
            print("Exiting program...")
            break


if __name__ == "__main__":
    main()
