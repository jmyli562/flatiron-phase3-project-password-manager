from sqlalchemy.orm import sessionmaker, make_transient
from models import User, Category, Entry, Tag, engine
from simple_term_menu import TerminalMenu

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

    print(f"User {username} added successfully!")


def user_menu(user):
    user_menu = TerminalMenu(
        ["View Passwords", "Create New Entry", "Update Password", "Logout"]
    )
    while True:
        user_selection = user_menu.show()
        if user_selection == 3:
            print("Logging out...")
            print(f"User {user.username} has successfully logged out.")
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
