from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Category, Entry, Tag, entry_tags, engine
from faker import Faker
import random

# creating a session
Session = sessionmaker(bind=engine)
session = Session()
# clearing any existing data in the database
session.query(Entry).delete()
session.query(Category).delete()
session.query(User).delete()
session.query(Tag).delete()
session.query(entry_tags).delete()
session.commit()

# creating a faker instance
faker = Faker()

# generating 10 sample users to fill the database
users = []

for i in range(10):
    user = User(
        username=faker.user_name(), password=faker.password(), email=faker.email()
    )
    users.append(user)

session.add_all(users)
session.commit()

# generating 10 sample categories
categories = [
    "Social Media",
    "Email services",
    "Financial Accounts",
    "Entertainment",
    "Online shopping",
    "Work",
    "Health and Fitness",
    "Travel",
    "Education",
]

used_category_names = set()  # Keep track of used category names

for _ in range(10):
    # Choose a category name that hasn't been used yet
    available_categories = [
        category for category in categories if category not in used_category_names
    ]
    if not available_categories:
        break  # No more unique categories available
    category_name = random.choice(available_categories)
    used_category_names.add(category_name)  # Mark category as used

    # Choose a random User instance from the users list
    user_instance = random.choice(users)

    category = Category(name=category_name, user=user_instance)
    session.add(category)

session.commit()

# Generate sample tags
tags = []
for _ in range(10):
    tag_name = faker.word()  # generating a name using faker
    existing_tag = (
        session.query(Tag).filter_by(name=tag_name).first()
    )  # quering the database to check if tag already exists
    if not existing_tag:  # if it doesn't exist, add to database
        tag = Tag(name=tag_name)
        tags.append(tag)

session.add_all(tags)
session.commit()

# generating 10 sample entries for a user
entries = []
categories = session.query(Category).all()  # retrieving all of the categories
for _ in range(10):
    category = random.choice(categories)  # selecting a random category object
    entry = Entry(
        website=faker.url(),
        username=faker.user_name(),
        password=faker.password(),
        notes=faker.sentence(),
        user=faker.random_element(users),
        category=category,
        created_at=faker.date_time_this_year(),
        updated_at=faker.date_time_this_year(),
    )
    num_tags = faker.random_int(min=1, max=3)
    entry.tags = faker.random_elements(tags, unique=True, length=num_tags)

    entries.append(entry)

session.add_all(entries)
session.commit()

print("Sample data has been seeded.")
