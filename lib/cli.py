from sqlalchemy.orm import sessionmaker, make_transient
from models import User, Category, Entry, Tag, engine
from simple_term_menu import TerminalMenu
from datetime import datetime
import getpass
import random

# Create the session
Session = sessionmaker(bind=engine)
session = Session()


def login():
    username = input("Please enter your username: ")
    password = getpass.getpass("Please enter your password: ")

    user = session.query(User).filter_by(username=username).first()

    if user and user.password == password:
        make_transient(user)
        print("Login successful!")
        user_menu(user)
    else:
        print("Invalid credentials. Please try logging in again.")
        return None


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
    user_entry = session.query(Entry).filter_by(user=user).all()

    # no saved passwords were found
    if not user_entry:
        print(f"User {user.username} has no saved passwords.")
        return

    print("\nSaved Passwords:")
    print("-" * 30)
    for index, entry in enumerate(user_entry, start=1):
        print(f"\nEntry {index}:")
        print(f"Website: {entry.website}")
        print(f"Username: {entry.username}")

        prompt_user = input("Reveal password for this site? (y/n): ")
        # prompt the user asking they would like to have their password shown in plain text or encrypted
        if (
            prompt_user.lower() == "y"
        ):  # if yes reveal password if no display password as asteriks
            print(f"Password: {entry.password}")
        else:
            print(f"Password: " + "*" * len(entry.password))
        print(f"Category: {entry.category.name}")
        print("-" * 30)
    print()


def create_entry(user):
    website = input("Please enter the website url: ")
    username = input("Please enter your username for that website: ")
    password = input("Please enter the password: ")
    note = input("Please type out a note for this website: ")
    name = input("Please enter the category name: ")

    # Checking if the category already exists for the logged in user
    category = session.query(Category).filter_by(name=name, user=user)
    # If is does not exist create a new category entry in database
    if not category:
        print("Category not found. Creating new category...")
        category = Category(name=name, user=user)
        session.add(category)
        session.commit()

    current_time = datetime.now()  # Get the current timestamp

    new_entry = Entry(
        website=website,
        username=username,
        password=password,
        notes=note,
        created_at=current_time,  # Set the created_at timestamp
        updated_at=None,  # Set the updated_at initially to NULL
        user=user,
        category=category,
    )
    session.add(new_entry)
    session.commit()
    print("New Entry has been created successfully!")


def generate_password():
    # Prompt user for password length, making sure that the input is an integer
    length = int(input("Enter desired password length: "))

    # Prompt user for including special characters
    include_special = input("Include special characters? (y/n): ")

    ascii = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    characters = ascii + digits
    if include_special.lower() == "y":
        print("Entered here")
        punctuation = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~."
        characters += punctuation

    # Generate and return password using random choice
    password = "".join(random.choice(characters) for i in range(length))
    return password


def update_password(user):
    website = input("Enter website for the password you want to update: ")
    prompt = input("Would you like to generate a secure password? [y/n]?")

    if prompt.lower() == "y":
        new_password = generate_password()  # calling generate password method
    else:
        new_password = input("Please enter the new password: ")

    entry = (
        session.query(Entry).filter_by(website=website, user=user).first()
    )  # retrieving the entry that needs it password updated
    if entry:  # checking if the entry exists
        entry.password = (
            new_password  # setting the attribute password to the new password
        )
        entry.updated_at = datetime.now()  # Update the updated_at timestamp
        session.commit()
        print("Password updated successfully!")
    else:
        print("Entry was not found. Password update failed.")


def view_categories(user):
    categories = (
        session.query(Category).filter_by(user=user).all()
    )  # querying the Category table to find categories that match the user

    if not categories:  # no categories were found that were created by the user
        print(f"No categories were found for user {user.username}")
    print("-" * 30)
    print("\nCategories:")
    print("-" * 30)

    category_options = []  # empty list that will hold options
    for category in categories:
        category_options.append(
            category.name
        )  # looping through the queries returned and appending category names to list

    category_menu = TerminalMenu(category_options)  # initializing Terminal Menu
    user_selection = category_menu.show()
    # print(f"You selected {category_options[user_selection]}!")

    selected_category = next(
        (
            category
            for category in categories
            if category.name
            == category_options[
                user_selection
            ]  # generator expression using next to find first category that matches
        ),
        None,
    )

    if selected_category:
        print(f"Viewing entries in category: {selected_category.name}\n")
        for entry in selected_category.entries:
            print(f"Website: {entry.website}")
            print(f"Username: {entry.username}")
            print(f"Password: {entry.password}")
            print("-" * 30)
    else:
        print("Category was not found.")


def delete_entry(user):
    # quering the Entry table and selecting the rows where user matches the user on the table
    user_entries = session.query(Entry).filter_by(user=user).all()

    # No entry was found
    if not user_entries:
        print("No entries found.")
        return

    choices = [
        entry.website for entry in user_entries
    ]  # using list comprehension to return the website names

    choice_menu = TerminalMenu(choices, title="Please select an entry to delete.")
    index = choice_menu.show()  # displaying the TerminalMenu

    if index is None:
        print("Password deletion was canceled.")
        return

    selected_entry = user_entries[index]  # getting the actual value using the index

    print("Deleting entry for: ", selected_entry.website)

    confirm_with_user = input("Are you sure you want to delete this entry? [y/n]")

    if confirm_with_user.lower() == "y":
        session.delete(selected_entry)
        session.commit()
        print("Entry was successfully deleted.")
    else:
        print("Password deletion was canceled.")


def add_tag_to_entry(user):
    website_prompt = input("Please enter the website you want to add a tag too.")
    tag_name = input("Please enter the tag name: ")

    entry_query = (
        session.query(Entry)
        .filter_by(website=website_prompt, user=user)
        .first()  # quering the Entry table to find a row where the website and user match
    )

    if entry_query:
        tag = (
            session.query(Tag).filter_by(name=tag_name).first()
        )  # returning the first row in the tag table where the name matches

        if not tag:  # tag was not found
            tag = Tag(name=tag_name)  # creating a new Tag instance
            session.add(tag)  # adding the tag to the session
            session.commit()  # comitting the new entry to the database

        if tag not in entry_query.tags:
            entry_query.tags.append(
                tag
            )  # adding the tag to the entry if not already added
            session.commit()
            print("Tag was successfully added to the Entry")
        else:
            print("Entry already has this Tag added to it")
    else:
        print("Entry was not found.")


def search_for_entry_by_tag(user):
    while True:  # Keep prompting the user until they enter a correct tag
        tag_name = input("Enter the tag name to search for: ")

        tag_name.strip()  # removing leading and trailing white space

        if len(tag_name) == 0:  # checking for empty input
            print("Tag name cannot be empty. Please try again")

        if (
            not tag_name.isalpha()
        ):  # checking if the input only contains alphabetical letters
            print("Tag name should only contain letters. Please try again.")
            continue
        break

    # fetching from the database all the entries that are associated with a specific tag for the currently logged in user

    entries_with_tags = (
        session.query(Entry)
        .filter(Entry.user == user)  # filtering the entries by user
        .join(
            Entry.tags
        )  # Joining the Entry table with the entry_tags table to access tags
        .filter(
            Tag.name == tag_name
        )  # filtering the entries to look for the entered tag
        .all()  # getting all the matched entries
    )
    # No tag was found that had a entry associated with it
    if not entries_with_tags:
        print(f"No associated entries were found with the tag '{tag_name}'")
        return

    print(f"These are the entries that were found with the tag '{tag_name}'")

    # looping through the returned query and printing information about the entry
    for entry in entries_with_tags:
        print("- Website:", entry.website)
        print("  Username:", entry.username)
        print("  Password:", entry.password)
        print("  Notes:", entry.notes)
        print("-" * 40)


def count_entries_by_tag(user):
    tag_name = input("Please enter the name of the tag that you want to count: ")

    tag = session.query(Tag).filter_by(name=tag_name).first()

    if not tag:  # tag was not found
        print(f"Tag '{tag_name}' not found.")
        return

    entries_with_tag = (
        session.query(Entry)
        .filter(Entry.user == user)  # Filter entries by user
        .join(Entry.tags)  # Join with the entry_tags table to access tags
        .filter(Tag.name == tag_name)  # Filter entries by the given tag name
        .count()  # Count the number of matching entries
    )

    print(f"Number of entries with tag '{tag_name}': {entries_with_tag}")


def get_avg_password_length(user):
    user_entries = (
        session.query(Entry).filter_by(user=user).all()
    )  # querying the Entry table for rows where the user match

    if not user_entries:  # a entry does not exist for the user
        print(f"User {user.username} has no entries.")
        return

    password_length = 0  # variable that will store the password length
    num_entries = len(user_entries)
    for entry in user_entries:
        password_length += len(
            entry.password
        )  # adding to the password length the length of each of the user's password

    average_length = password_length / num_entries  # calculating the average
    print(f"Average password length for {user.username}: {average_length}")


def get_total_num_entries(user):
    total_entries = (
        session.query(Entry).filter_by(user=user).count()
    )  # using count aggregate method to count the number of entries for a user
    print(f"Total number of entries for {user.username}: {total_entries}")


def user_menu(user):
    user_menu = TerminalMenu(
        [
            "Manage Passwords",
            "Manage Entries",
            "Manage Categories",
            "Manage Tags",
            "Logout",
        ]
    )
    while True:
        user_selection = user_menu.show()
        if user_selection == 0:
            password_submenu(user)
        elif user_selection == 1:
            entry_submenu(user)
        elif user_selection == 2:
            category_submenu(user)
        elif user_selection == 3:
            tag_submenu(user)
        elif user_selection == 4:
            print("Logging out...")
            print(f"User {user.username} has been successfully logged out.")
            break


def password_submenu(user):
    password_menu = TerminalMenu(
        [
            "View Passwords",
            "Update Password",
            "Get Average Password Length",
            "Back",
        ]
    )
    while True:
        user_selection = password_menu.show()
        if user_selection == 0:
            view_passwords(user)
        elif user_selection == 1:
            update_password(user)
        elif user_selection == 2:
            get_avg_password_length(user)
        elif user_selection == 3:
            user_menu(user)


def entry_submenu(user):
    entry_menu = TerminalMenu(
        [
            "Create new Entry",
            "Delete Entry",
            "Get total Entries",
            "Back",
        ]
    )
    while True:
        user_selection = entry_menu.show()
        if user_selection == 0:
            create_entry(user)
        elif user_selection == 1:
            delete_entry(user)
        elif user_selection == 2:
            get_total_num_entries(user)
        elif user_selection == 3:
            user_menu(user)


def category_submenu(user):
    category_menu = TerminalMenu(
        [
            "View Categories",
            "Create Category",
            "Back",
        ]
    )
    while True:
        user_selection = category_menu.show()
        if user_selection == 0:
            view_categories(user)
        elif user_selection == 1:
            create_category(user)
        elif user_selection == 2:
            user_menu(user)


def tag_submenu(user):
    tag_menu = TerminalMenu(
        [
            "Add Tag to Entry",
            "Search Entry by Tag",
            "Count Entries by Tag",
            "Back",
        ]
    )
    while True:
        user_selection = tag_menu.show()
        if user_selection == 0:
            view_categories(user)
        elif user_selection == 1:
            delete_entry(user)
        elif user_selection == 2:
            get_total_num_entries(user)
        elif user_selection == 3:
            user_menu(user)


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
