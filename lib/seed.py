from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Category, Entry, Tag, engine
from faker import Faker
import random

# creating a session
Session = sessionmaker(bind=engine)
session = Session()
# clearing any existing data in the database
session.query(Entry).delete()
session.query(Category).delete()
session.query(User).delete()
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

for _ in range(10):
    category_name = random.choice(categories)  # Select a random category name
    user = random.choice(users)  # Select a random user object

    category = Category(name=category_name, user=user)
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
for _ in range(10):
    entry = Entry(
        website=faker.url(),
        username=faker.user_name(),
        password=faker.password(),
        notes=faker.sentence(),
        user=faker.random_element(users),
        category=faker.random_element(user.categories),
        created_at=faker.date_time_this_year(),
        updated_at=faker.date_time_this_year(),
    )
    num_tags = faker.random_int(min=1, max=3)
    entry.tags = faker.random_elements(tags, unique=True, length=num_tags)

    entries.append(entry)

session.add_all(entries)
session.commit()

print("Sample data has been seeded.")
