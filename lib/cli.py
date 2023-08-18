from sqlalchemy.orm import sessionmaker, make_transient
from models import User, Category, Entry, Tag, engine
from simple_term_menu import TerminalMenu
from datetime import datetime

# Create the session
Session = sessionmaker(bind=engine)
session = Session()


def login():
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")

    user = session.query(User).filter_by(username=username).first()

    if user and user.password == password:
        make_transient(user)
        print("Login successful!")
        user_menu(user)
    else:
        print("Invalid credentials. Please try again")
        login()


def add_user():
    email = input("Please enter your email: ")
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")

    user = User(username=username, password=password, email=email)
    session.add(user)
    session.commit()

    print(f"User {username} added successfully!")


def view_passwords(user):
    # retrieving all of the entries that match the filter
    user_entry = session.query(Entry).filter_by(user_id=user.id).all()

    # no saved passwords were found
    if not user_entry:
        print(f"User {user.username} has no saved passwords.")
        return
    print("\nSaved Passwords:")
    for index, entry in enumerate(user_entry, start=1):
        print(f"\nEntry {index}:")
        print(f"Website: {entry.website}")
        print(f"Username: {entry.username}")
        print(f"Password: {entry.password}")
        print(f"Category: {entry.category.name}")
        print("-" * 30)
    print()


def create_entry(user):
    website = input("Please enter the website url: ")
    username = input("Please enter your username for that website: ")
    password = input("Please enter the password: ")
    note = input("Please type out a note for this website: ")
    category = input("Please enter the category name: ")


def user_menu(user):
    user_menu = TerminalMenu(
        [
            "View Passwords",
            "Create New Entry",
            "Update Password",
            "View Categories",
            "Add Tag to Entry",
            "Search Entry by Tag",
            "Logout",
        ]
    )
    while True:
        user_selection = user_menu.show()
        if user_selection == 0:
            view_passwords(user)
        elif user_selection == 1:
            create_entry(user)
        elif user_selection == 2:
            pass
        elif user_selection == 3:
            pass
        elif user_selection == 4:
            pass
        elif user_selection == 5:
            pass
        elif user_selection == 6:
            print("Logging out...")
            print(f"User {user.username} has been successfully logged out.")
            break


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
    print(
        """
=======================================================================================================================================
=======================================================================================================================================

██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗     ███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗██████╗ 
██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗    ████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗
██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║    ██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██████╔╝
██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║    ██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██╔══██╗
██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝    ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║  ██║
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
=======================================================================================================================================
=======================================================================================================================================
    """
    )

    main()
